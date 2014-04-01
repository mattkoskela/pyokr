from flask import Flask, render_template


app = Flask(__name__)
app.config.from_pyfile('okr.config')


@app.route('/')
def index():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(port=5001)
