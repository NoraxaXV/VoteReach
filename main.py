from flask import Flask
from flask import render_template
from flask import request

app = Flask('app')


@app.route("/linker")
def linkPage():
  
  return render_template("linkerIndex.html")


@app.route("/")
def main():
  return render_template("index.html")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
  return render_template('sign_up.html')


@app.route("/leaderboard")
def leaderboard():
  return render_template("leaderboard.html")

@app.route("/signup/confirm", methods=['POST', 'GET'])
def sendEmail():
  if request.method == "POST":
    return render_template("check_email.html", username=request.form["username"])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
