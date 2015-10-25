from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<name>')
def hello(name):
    return "Hello " + name.capitalize()

if __name__ == '__main__':
    app.run(debug = True)
    # or
    # app.debug = True
    # app.run()
