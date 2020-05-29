from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "gfsug@!$!#%$HI&&(&*"
app.permanent_session_lifetime = timedelta(minutes = 5)

@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['userName']
        session["user"] = user  #setup a session data based on the  information that aratype by user, this session is working as a dictionary 
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
            
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():   
    session.pop("user",  None)
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)