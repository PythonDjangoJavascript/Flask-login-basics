from basic_login import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# to allow flask to load curr user and fetch their id
@login_manager.user_loader
def load_user(user_id):
    """Returns current loggedin user"""

    return User.query.get(user_id)

# Database Modelsdv ---------->


class User(db.Model, UserMixin):
    """Define user model and provide all helpful methods for authentications"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(80), unique=True, index=True)
    hasshed_pass = db.Column(db.String(150))

    def __init__(self, username, email, password):
        """Initializes user table"""
        self.username = username
        self.email = email
        self.hasshed_pass = generate_password_hash(password)

    def check_password(self, password):
        """Returns true if password is correct"""

        return check_password_hash(self.hasshed_pass, password)
