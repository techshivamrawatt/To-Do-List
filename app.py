from flask import Flask,render_template,request,redirect,url_for
from dbconnection import save_work,view_data,delete_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods=["POST"])
def submit():
    work =  request.form.get("work")

    save_work(work)

    return render_template("home.html")

@app.route("/view", methods=["GET"])
def view():
    datas = view_data()
    return render_template("view.html", datas=datas)

@app.route("/delete/<int:id>")
def delete(id):
    delete_data(id)
    return redirect(url_for("view"))
