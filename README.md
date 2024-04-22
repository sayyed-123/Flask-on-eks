# Flask-on-eks
### Create EC2 Instance as Workspace ( machine-type = t2.small)
## Prerequisites:
### 1 - install kubectl

  https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux
  
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
      curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
      echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
      sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
      chmod +x kubectl
      mkdir -p ~/.local/bin
      mv ./kubectl ~/.local/bin/kubectl


### 2 - install eksctl

  https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-eksctl.html
  
    curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
    sudo mv /tmp/eksctl /usr/local/bin
    eksctl version
### 3 - install AWS CLI

  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

( Note : for ubuntu install 'unzip' binary  $ sudo apt install unzip )

      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      
      unzip awscliv2.zip
      sudo ./aws/install
      aws --version
### 4 - Authenticate through IAM ( $ aws configure )
![image](https://github.com/sayyed-123/Flask-on-eks/assets/166358159/e818224f-5137-4395-b274-4d15e921570d)

### 5 - install docker

  https://docs.docker.com/engine/install/ubuntu/

![image](https://github.com/sayyed-123/Flask-on-eks/assets/166358159/a2d642e5-657c-4aeb-8882-ff8b7ca0e59b)

      sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

![image](https://github.com/sayyed-123/Flask-on-eks/assets/166358159/33315c77-a1bb-4336-89f2-99f87cd47332)


### create your ECR Repo
      aws ecr create-repository --repository-name <REPO-NAME> --region us-west-2
### Authenticate your docker to ecr
      aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 440896245143.dkr.ecr.us-west-2.amazonaws.com
### docker Build
       docker build -t <app-name> .
### docker tag
       docker tag <IMAGE-NAME>:latest <ACCOUNTID>.dkr.ecr.us-west-2.amazonaws.com/<ECR-REPO-NAME>:latest
### docker push
       docker push <ACCOUNTID>.dkr.ecr.us-west-2.amazonaws.com/<ECR-REPO-NAME>:latest
## Create EKS Cluster
      eksctl create cluster --name <CLUSTER-NAME> --region <REGION> --node-type <MACHINE-TYPE> --nodes-min 2 --nodes-max 3
### Create our deployment
       kubectl apply -f deployment.yaml
### Create service
       kubectl apply -f service.yaml
### access Flask app
      kubectl get services ( paste url to browser to access the Flask application)...

==========================================================================

https://cmakkaya.medium.com/kubernetes-creating-and-testing-a-horizontal-pod-autoscaling-hpa-in-kubernetes-cluster-548f2378f0c3

https://katharharshal1.medium.com/kubernetes-cluster-autoscaling-ca-using-aws-eks-4aab8c89f9a1
## OR
### Create cluster with Autoscaling
    ( For Horizontal Pod Scaling & Cluster Autoscaling )
      eksctl create cluster --name <CLUSTER-NAME> --region us-west-2 --managed --asg-access 
https://katharharshal1.medium.com/kubernetes-cluster-autoscaling-ca-using-aws-eks-4aab8c89f9a1
### Deploy " Cluster Autoscaler" to your cluster
        kubectl apply -f cluster-autoscaler-autodiscover.yaml
### Add the " cluster-autoscaler.kubernetes.io/safe-to-evict "
        kubectl -n kube-system annotate deployment.apps/cluster-autoscaler cluster-autoscaler.kubernetes.io/safe-to-evict="false"
### Edit the cluster autoscaler deployment 
        kubectl -n kube-system edit deployment.apps/cluster-autoscaler
### replace YOUR-CLUSTER-NAME  and  add the following options
       --balance-similar-node-group
       --skip-nodes-with-system-pods=false
### NOTE : cluster autoscaler version sould match with your kubernetes cluster version    
### Deploy metrics-server
      kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
      kubectl get hpa
      kubectl get hpa <DEPLOYMENT-NAME> --watch

##



