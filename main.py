from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    return "weliv mubarak chuv!"


if __name__ == '__main__':
    app.run(debug=True)