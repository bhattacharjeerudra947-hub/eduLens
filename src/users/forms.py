from wtforms import (StringField, TelField, EmailField, SubmitField, 
                     PasswordField, BooleanField)
from wtforms.validators import DataRequired, Regexp, Length, EqualTo
from flask_wtf import FlaskForm


class RegistrationForm(FlaskForm):

    name = StringField("Student's Name", validators=[DataRequired(), 
                                            Regexp(r'^[A-Za-z]+$', 
                                            message="Enter a valid name!")])
    roll_no = TelField("Roll Number", validators=[DataRequired(), 
                                            Regexp(r'^[0-9]{5}$', 
                                            message="Enter a valid roll number!")])
    department = StringField("Department", validators=[DataRequired(), 
                                            Regexp(r'^[A-Za-z]+$', 
                                            message="Enter a valid department!")])
    phone = TelField("Contact Number", validators=[DataRequired(), 
                                            Regexp(r'^[0-9]{10}$', 
                                            message="Enter a valid contact number!")])
    email = EmailField("Personal Email ID", validators=[DataRequired(), 
                                                Regexp(r'^[a-z0-9._+%-]+@[a-z0-9.-]+\.[a-z]{2,}$', 
                                                message="Enter a valid email ID!")])
    current_password = PasswordField("Account Password", validators=[DataRequired(), 
                                            Length(min=8)])
    confirm_passwd = PasswordField("Confirm Password", validators=[DataRequired(), 
                                            Length(min=8), EqualTo('current_password')])
    submit = SubmitField("Create Account")


class LoginForm(FlaskForm):

    name = StringField("Student's Name", validators=[DataRequired(), 
                                            Regexp(r'^[A-Za-z]+$', 
                                            message="Enter a valid name!")])
    roll_no = TelField("Roll Number", validators=[DataRequired(), 
                                            Regexp(r'^[0-9]{5}$', 
                                            message="Enter a valid roll number!")])
    current_password = PasswordField("Account Password", validators=[DataRequired(), 
                                            Length(min=8)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
