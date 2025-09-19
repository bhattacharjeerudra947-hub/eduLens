import os

class Config:

    passwd = "newpassword"

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"mysql://root:{passwd}@localhost:3306/student_data"
