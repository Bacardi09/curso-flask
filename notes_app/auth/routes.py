from flask import Blueprint, request, render_template, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        if username == "admin":
            session["user"] = username
            return redirect (url_for("notes.index"))
        else:
            flash("Usuario no existe", "error")
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("Te has desconectado correctamente", "success")
    return redirect(url_for("auth.login"))