from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Rendering a html file
# @app.route("/<name>")
# def home(name):
#     return render_template("index.html", content = name, r=4)

#Rendering a list
@app.route("/")
def home():
    return render_template("index.html",content = ["Apple", "Pineapple", "Pears", "Graps"])

if __name__ == "__main__":
    app.run()
