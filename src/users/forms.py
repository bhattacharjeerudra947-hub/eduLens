from wtforms import StringField, TelField, EmailField, SubmitField
from wtforms.validators import DataRequired, Regexp
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
    submit = SubmitField("Create Account")
