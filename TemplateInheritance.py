from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("templateinheritance.html")

@app.route("/test")
def test():
    return render_template("test.html",content = "Testing1")

if __name__ == "__main__":
    app.run(debug = True)