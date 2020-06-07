from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "gfsug@!$!#%$HI&&(&*"
app.permanent_session_lifetime = timedelta(minutes = 5)

#setup a configuration properties for app to define some stuff with the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#setup a new database object
db = SQLAlchemy(app)

#create a modelwhich we can store information
class users(db.Model):
    #properties are write as class attributes
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
 
    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['userName']
        session["user"] = user  #setup a session data based on the  information that are type by user, this session is working as a dictionary 

        #when the user types the name,check whether the user exists, if not create it
        found_user = users.query.filter_by(name = user).first()
        #found_user = users.query.filter_by(name = user).delete()

        # for user in found_user:
        #     user.delete()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user,"")#passing the information that want to setup the user
            #add that created user into the database  
            db.session.add(usr)
            db.session.commit()#must commit every time we change the database

        flash("login successful!") 
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in")  
            return redirect(url_for("user"))
            
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name = user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved")   
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email = email)
    else:
        flash("You are not logged in!") 
        return redirect(url_for("login"))

@app.route("/logout")
def logout():  
    if "user" in session:
        user = session["user"]
        flash("You have been logged out!", "info") 
    session.pop("user",  None)
    session.pop("email", None)
    return redirect(url_for("login"))
 
if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)