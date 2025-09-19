from flask_login import UserMixin
from src import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    
    try:
        return User.query.get(int(user_id)) if user_id else None
    except (ValueError, TypeError):
        return None


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    roll_no = db.Column(db.String(7), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    current_passwd = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"('{self.name}', '{self.roll_no}', '{self.email}')"
    