from basic_login import app, db
from basic_login.models import User
from basic_login.forms import LoginForm, RegistrationForm

from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user


@app.route('/')
def index():
    """Renders home page"""
    return render_template('index.html')


@app.route('/welcome')
@login_required
def welcome():
    """Welcome loggedin user"""
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    """Log out authenticated user"""
    logout_user()

    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Renders login form and login user"""

    form = LoginForm()

    if form.validate_on_submit():
        """After submission of valid input"""
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            """password is corrent and user exists"""

            login_user(user)
            flash("Successfully logged in")

            # If user forced to login page for tryting to access other page
            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = url_for('welcome')
            return redirect(next)

            # render if form is not valid or access loginpage
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Render and Register new user"""

    form = RegistrationForm()

    if form.validate_on_submit():
        """When user submit a valid registration form"""

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )

        # now save user to the database
        db.session.add(user)
        db.session.commit()

        flash("Registration Successful, Thank you for registration")
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
