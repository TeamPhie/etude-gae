from flask import Flask, request, render_template
from db import Session, Authentication

app = Flask(__name__)

global_list = []


@app.route('/', methods=["GET"])
def hello():
    return render_template("authentication_login.html")


@app.route('/authentication_top', methods=["GET", "POST"])
def authentication_top():
    # session = Session()

    posted_id = request.form["user_id"]
    posted_password = request.form["password"]
    id = Authentication.id.all()
    for i in id:
        if posted_id == i:
            password = Authentication.password.all()
            for p in password:
                if posted_password == p:
                    return render_template("goodjob.html")
                else:
                    return render_template("bad1.html")
        else:
            return render_template("bad2.html")
