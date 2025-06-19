from flask import Flask, url_for, render_template
from dotenv import load_dotenv
import os

# load the environment varibales
load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def root():
    return render_template("home.html")

debug_mode = os.getenv("FLASK_DEBUG", "0") == "1"
if __name__ == '__main__':
    app.run(debug=debug_mode)