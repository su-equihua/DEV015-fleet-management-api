from flask import Flask

#Crear una instancia en la clase Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"