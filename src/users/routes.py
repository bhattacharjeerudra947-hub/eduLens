from flask import (Blueprint, render_template, redirect, flash, url_for, 
                   request)
from flask_login import login_user, logout_user, current_user
from datetime import timedelta

from src.users.forms import RegistrationForm, LoginForm
from src.models import User
from src import bcrypt, db

users = Blueprint('users', __name__)

@users.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_passwd = bcrypt.generate_password_hash(form.current_password.data).decode('utf-8')

        user = User(
            name=form.name.data,
            roll_no=form.roll_no.data,
            department=form.department.data,
            phone=form.phone.data,
            email=form.email.data,
            current_passwd=hashed_passwd
        )

        db.session.add(user)
        db.session.commit()

        flash("You have been registered successfully!", 'success')
        return redirect(url_for("main.root_route"))

    return render_template("registration.html", form=form, title="Registration")


@users.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        
        user = User.query.filter_by(roll_no=form.roll_no.data).first()
        print(user)

        if user.name == form.name.data and user.roll_no == form.roll_no.data\
        and bcrypt.check_password_hash(user.current_passwd, form.current_password.data):
            
            login_user(user, remember=form.remember.data, duration=timedelta(days=30))
            next_page = request.args.get('next')

            flash("You have been logged in successfully!", 'success')
            return redirect(next_page) if (next_page) else redirect(url_for("main.root_route"))
        
        else:
            flash("Invalid credentials! Please try again!", 'danger')

    return render_template("login.html", title="Login", form=form)


@users.route("/statistics")
def statistics():

    return render_template("statistics.html", title="Student Stats")


@users.route("/logout")
def logout():

    logout_user()
    return redirect(url_for('main.root_route'))
