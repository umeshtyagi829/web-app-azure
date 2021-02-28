from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, Everyone!, This is Umesh  <img src='https://imagest.blob.core.windows.net/myc12/images.jpg' width='200'  height='300'/></h1>"
