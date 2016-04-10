from flask import Blueprint, render_template


main = Blueprint("main", __name__)


@main.route("/")
def root():
    return render_template("main/root.html")
