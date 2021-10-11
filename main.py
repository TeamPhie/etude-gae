from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

global_list = []
dt_list = []

@app.route('/', methods=["GET"])
def hello():
    information = "TODOを入力"
    dt = datetime.now()
    return render_template("index.html", information=information, dt=dt)


@app.route('/additem', methods=["GET", "POST"])
def add_item():
    # print(f"Form data: {dict(request.form)}")
    contents = request.form["contents"]
    global_list.append(contents)
    dt = datetime.now()
    dt_list.append(dt)
    return render_template("index.html", global_list=global_list, dt_list=dt_list)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)