from flask_login import UserMixin
from src import db, login_manager

@login_manager.user_loader
def load_user(id):
    try:
        return User.query.get(int(id)) if id else None
    except (ValueError, TypeError):
        return None


class User(db.Model, UserMixin):

    id = db.Column()