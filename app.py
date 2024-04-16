from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

#@app.route('/')
#def hello():
#    return "hello Wrld : Flask app is running successfully :"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)