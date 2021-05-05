from flask import Flask, render_template


app = Flask(__name__)


@app.route("/index")
def index():
    logedin = False
    return render_template("index.html", logedin=logedin)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(port="5001", use_reloader=True)