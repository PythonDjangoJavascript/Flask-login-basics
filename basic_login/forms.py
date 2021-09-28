from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from basic_login.models import User


# Flask Forms
class RegistrationForm(FlaskForm):
    """Define User Reg Form"""

    email = StringField("Enter Your Email", validators=[
                        DataRequired(), Email(), ])
    username = StringField("Enter Your User Name",
                           validators=[DataRequired(), ])
    password = PasswordField(
        "Enter Your Password",
        validators=[
            DataRequired(),
            EqualTo('password_confirm', message="Password Must match"),
        ]
    )
    password_confirm = PasswordField(
        "Confirm Password", validators=[DataRequired(), ])
    submit = SubmitField()

    def validate_email(self, field):
        """Cehck email is already registered"""
        if User.query.filter_by(email=field.data).first():
            """If its output is not none rise a error"""

            raise ValidationError(
                "Email Already Registered"
            )

    def validate_username(self, field):
        """Check username already exists in the database"""
        if User.query.filter_by(username=field.data).first():
            # User username already exists
            raise ValidationError(
                "User name already taken, Please try different one!"
            )


class LoginForm(FlaskForm):
    """Define Login Form"""

    email = StringField("Enter your Email", validators=[
                        DataRequired(), Email(), ])
    password = PasswordField("Enter your Password",
                             validators=[DataRequired(), ])
    submit = SubmitField()
