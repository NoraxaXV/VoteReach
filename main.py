#   This is the code for the server

#Imports modules
import os

from flask import Flask, url_for, redirect
from flask import render_template
from flask import request

#Inmport email modules
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Creates the server object
app = Flask("app")

# Gets config file
app.config.from_pyfile('config.py')


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
      #This contains the email to be sent
      message = Mail(
        from_email="asmith10@dekalbcentral.net",
        to_emails=request.form["email"],
        subject="Here is the link to the website!",
        html_content='''
        <p>Thanks for doing this, %s! Now go, share this, and get as many clicks as you can! </p>
        <a href="https://votereach-1.aaronsmith8.repl.co/register-to-vote">https://www.usa.gov/register-to-vote</a>
        ''' %request.form["username"])
      #This sends the email
      try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        sg.send(message)
        return render_template("check_email.html", username=request.form["username"]
        )
      except Exception as e:
        return e.message

@app.route("/register-to-vote")
def updateLink():
  return redirect("https://www.usa.gov/register-to-vote")

#Finally, start up the server
if __name__ == "__main__":
    app.run(host="0.0.0.0")
