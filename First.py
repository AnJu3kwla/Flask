from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

#Redirecting 
# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))

@app.route("/admin")
def admin():
    return redirect(url_for("user", name = "Admin!"))

if __name__ == "__main__":
    app.run()