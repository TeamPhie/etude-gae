from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello():
    information = 0
    return render_template("index.html", information=information)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
