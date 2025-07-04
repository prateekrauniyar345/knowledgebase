from flask import Flask, url_for, render_template
from dotenv import load_dotenv
import os
import pprint

# load the environment varibales
load_dotenv()

app = Flask(__name__,
            template_folder='templates', 
            static_folder= 'static'
            )

# default page
@app.route("/", methods=["POST", "GET"])
def root():
    return render_template("home.html")


# features page
@app.route("/features", methods=["POST", "GET"])
def features():
    return render_template("features.html")

# pricing page
@app.route("/pricing", methods=["POST", "GET"])
def pricing():
    return render_template("pricing.html")

# contact us page
@app.route("/contactus", methods=["POST", "GET"])
def contactus():
    return render_template("contactus.html")

# Auths
@app.route("/auths/login", methods=["POST", "GET"])
def login():
    return render_template("auths/login.html")

@app.route("/auths/register", methods=["POST", "GET"])
def register():
    return render_template("auths/register.html")


debug_mode = os.getenv("FLASK_DEBUG", "0") == "1"
# print("debug mode is : ", debug_mode)
pprint.pprint(app.jinja_loader.searchpath)
if __name__ == '__main__':
    app.run(debug=debug_mode)