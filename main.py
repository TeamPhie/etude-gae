from flask import Flask, request, render_template
from datetime import datetime
from db import Session, ToDo

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
    session = Session()
    posted_form = request.form["contents"]
    todo = ToDo(contents=posted_form)
    session.add(todo)
    session.commit()
    contents = session.query(ToDo).all()
    dt = datetime.now()
    dt_list.append(dt)
    return render_template("index.html", global_list=global_list, dt_list=dt_list, contents=contents)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
