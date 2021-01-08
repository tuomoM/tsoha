from app import app
from flask import Flask, render_template, request, redirect
import users
import vocabulary

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["get","post"])
def loginPage():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Invalid userid or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["post"])
def register():
  
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")    

@app.route("/maintain")
def maintain_menu():
    if users.user_type():
        return render_template("maintainMenu.html")
    else:
        return render_template("error.html", message = "Oops, something went wrong!")

@app.route("/maintainNouns", methods = ["post","get"])
def maintain_nouns():
    if users.user_type():
        if request.method == "GET":
            return render_template("maintainNouns.html", nouns = vocabulary.get_nouns() )
        if request.method == "POST":
            noun = request.form["noun"]
            gender = request.form["gender"]
            english = request.form["english"]
            if vocabulary.insert_noun(gender,noun,english):
                return render_template("maintainNouns.html", nouns = vocabulary.get_nouns() )

            else:
                return render_template("error.html", message = "update failed")
    else:
       
        return render_template("error.html", message = "Not authorized.")
