# Flask-on-eks
### Create EC2 Instance as Workspace ( machine-type = t2.small)
## Prerequisites:
### 1 - install kubectl

  https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux

    $ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  
    $ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
  
    $ echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check

### 2 - install eksctl

  https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-eksctl.html

    $ curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
  
    $ sudo mv /tmp/eksctl /usr/local/bin
  
    $ eksctl version
### 3 - install AWS CLI

  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

( Note : for ubuntu install 'unzip' binary  $ sudo apt install unzip )

    $ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    
    $ unzip awscliv2.zip
    
    $ sudo ./aws/install
    
    $ aws --version
### 4 - Authenticate through IAM ( $ aws configure )
![image](https://github.com/sayyed-123/Flask-on-eks/assets/166358159/e818224f-5137-4395-b274-4d15e921570d)

### 5 - install docker

  https://docs.docker.com/engine/install/ubuntu/

![image](https://github.com/sayyed-123/Flask-on-eks/assets/166358159/a2d642e5-657c-4aeb-8882-ff8b7ca0e59b)

    $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

![image](https://github.com/sayyed-123/Flask-on-eks/assets/166358159/33315c77-a1bb-4336-89f2-99f87cd47332)


### create your ECR Repo
    $ aws ecr create-repository --repository-name <REPO-NAME> --region us-west-2
### Authenticate your docker to ecr
    $ aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 440896245143.dkr.ecr.us-west-2.amazonaws.com
### docker Build
    $ docker build -t <app-name> .
### docker tag
    $ docker tag <IMAGE-NAME>:latest <ACCOUNTID>.dkr.ecr.us-west-2.amazonaws.com/<ECR-REPO-NAME>:latest
### docker push
    $ docker push <ACCOUNTID>.dkr.ecr.us-west-2.amazonaws.com/<ECR-REPO-NAME>:latest
### Create our deployment
    $ kubectl apply -f deployment.yaml
### Create service
    $ kubectl apply -f service.yaml
### access Flask app
    $ kubectl get services ( paste url to browser to access the Flask application)



