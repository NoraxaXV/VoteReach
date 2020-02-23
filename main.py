#   This is the code for the server


#Imports only the functions that we need
from flask import Flask, redirect, url_for, render_template, make_response, request, flash

#Inmport email modules
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#Imports modules
import os
from datareader import *

# Creates the server object (Doesn't start it yet, though)
app = Flask("app")
app.secret_key=os.getenv("APP_SECRET_KEY")
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
    username=request.form["username"]
    if getUserClicks(username) != -1:
      flash("Username taken.")
      return redirect(url_for("signup"))
    else:
      addUser(username)
    
    #This contains the email to be sent
    message = Mail(
      from_email="asmith10@dekalbcentral.net",
      to_emails=request.form["email"],
      subject="Here is the link to the website!",
      html_content='''
      <p>Thanks for doing this, %s! Now go, copy/paste the link below, share this, and get as many clicks as you can! </p>
      <a href="https://votereach.aaronsmith8.repl.co/register-to-vote/%s">https://votereach.aaronsmith8.repl.co/register-to-vote/%s</a>
      ''' % (username,username,username))
      
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
  if getUserClicks(id) == -1:
    return "Link no longer valid!"
  else:
    incrementUserClicks(id)   
  
  return redirect("https://www.usa.gov/register-to-vote")



#______________________________________Finally, start up the server
if __name__ == "__main__":
  app.run(host="0.0.0.0")
