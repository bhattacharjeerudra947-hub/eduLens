import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    passwd = "newpassword"

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"mysql://root:newpassword@localhost:3306/student_data"

