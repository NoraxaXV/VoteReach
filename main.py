#   This is the code for the server

#Imports modules
from flask import Flask
from flask import render_template
from flask import request

#Creates the server object
app = Flask("app")


#This returns default page
@app.route("/")
def main():
    return render_template("index.html")


#This returns the link page
@app.route("/linker")
def linkPage():
    return render_template("linkerIndex.html")


#This returns the signup page and gets form requests
@app.route("/signup", methods=["GET"])
def signup():
    return render_template("sign_up.html")


#This returns the leaderboard
@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")


#This is the page that will send the email
@app.route("/signup/confirm", methods=["POST", "GET"])
def sendEmail():
    if request.method == "POST":
        return render_template(
            "check_email.html", username=request.form["username"])


#Finally, start up the server
if __name__ == "__main__":
    app.run(host="0.0.0.0")
