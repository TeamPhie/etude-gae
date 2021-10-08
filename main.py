from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "This is GET method!"
    if request.method == "POST":
        user_id = request.get_json()["user_id"]
        return f'User ID: {user_id}'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
