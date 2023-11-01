from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return("<p1>home</p>")
@app.route("/login")
def login():
    return("<p>login page</p>")

if __name__ == "__main__":
    app.run(debug=True)