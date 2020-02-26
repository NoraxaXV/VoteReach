#   This is the code for the server


#Imports only the functions that we need
from flask import Flask, redirect, url_for, render_template, make_response, request, flash

#Inmport email modules
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#Imports modules
import os
from datareader import *
import datetime


# Creates the server object (Doesn't start it yet, though)
app = Flask("app")
app.secret_key=os.getenv("APP_SECRET_KEY")

# Gets config file
app.config.from_pyfile('config.py')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#This returns default page
@app.route("/")
def main():
  return render_template("index.html", data=getData(num=5))


#This returns the link page
@app.route("/linker")
def linkPage():
  return render_template("linkerIndex.html")

#This returns the link page
@app.route("/test_bed")
def test_bed():
  return render_template("test_bed.html")

#This returns the signup page and gets form requests
@app.route("/signup/<msg>", methods=["GET"])
def signup(msg):
  if msg != "enter":
    flash("Username taken! Please try a different name")
  return render_template("sign_up.html")


#This returns the leaderboard
@app.route("/leaderboard")
def leaderboard():
  return render_template("leaderboard.html", data=getData())


#This is the page that will send the email
@app.route("/confirm", methods=["POST", "GET"])
def sendEmail():
  if request.method == "POST":
    username=request.form["username"]
    if getUserClicks(username) != -1:
      return redirect(url_for("signup", msg="user-name-taken"))

    addUser(username)
    
    #This contains the email to be sent
    message = Mail(
      from_email="asmith10@dekalbcentral.net",
      to_emails=request.form["email"],
      subject="Here is the link to the website!",
      html_content=render_template("email.html", username=username))
      
      #This sends the email
    try:
      sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
      sg.send(message)
      resp =  make_response(render_template("check_email.html", username=username))
      return resp
    except Exception as e:
      return e.message


#Basically, the link first goes to our website. 
# We record that the link was clicked on, 
#Then we redirect the clicker to the registration website
@app.route("/register-to-vote/<id>")
def updateLink(id):

  cookie=request.cookies.get(id)
  userExists=(getUserClicks(id) != -1)
  
  if userExists == True and cookie != "exists":
    incrementUserClicks(id)   

  resp=redirect("https://www.usa.gov/register-to-vote")
  resp.set_cookie(id, "exists", expires=datetime.datetime.now() + datetime.timedelta(days=7))
  return resp

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers["Cache-Control;"] = "public, max-age=0"
    return r

#______________________________________Finally, start up the server
if __name__ == "__main__":
  app.run(host="0.0.0.0")
