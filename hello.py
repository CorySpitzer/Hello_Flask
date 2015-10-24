from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h>Hello, Oh <b>World!</b></h>"

@app.route('/<name>')
def hello(name):
    return "Hello " + name.capitalize()

if __name__ == '__main__':
    app.run(debug = True)
    # or
    # app.debug = True
    # app.run()
