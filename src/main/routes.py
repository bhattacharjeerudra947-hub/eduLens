from flask import Blueprint, render_template
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route("/")
def root_route():

    if current_user.is_authenticated:
        return render_template("dashboard.html", title="Dashboard", root="Dashboard")

    return render_template("home.html", title="Home", root="Home")

@main.route("/about")
def about():

    return render_template("about.html", title="About Us")
