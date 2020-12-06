import os
from app import db
from app import app
from functools import wraps
from flask_wtf import FlaskForm
from wtforms.validators import (InputRequired, Length, DataRequired)
from wtforms import (StringField, PasswordField, SelectField)
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (render_template, url_for, request, flash, redirect)
from flask_login import (
    LoginManager, UserMixin, login_user,
    login_required, logout_user, current_user
)


# pwd = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80))
    level = db.Column(db.String(5))

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

class IndexForm(FlaskForm):
    tweet_text = StringField('Tweet_Text', validators=[InputRequired(), Length(min=2, max=35)]) # NOQA
    location = StringField('Location', validators=[InputRequired(), Length(min=1, max=80)]) # NOQA
    description = StringField('Description', validators=[InputRequired(), Length(min=1, max=80)]) # NOQA



@app.route('/', methods=['GET', 'POST'])
# @login_required
def index():
    form = IndexForm()
    tweet_text = form.tweet_text.data
    location = form.location.data
    description = form.description.data
    if form.validate_on_submit():

        flash('Is not IO')
    
        print(tweet_text)
        print(location)
        print(description)

    return render_template('index.html',form=form) # NOQA


@app.route('/dashboard', methods=['GET', 'POST'])
# @login_required
def dashboard():
    return render_template('dashboard.html') # NOQA

@app.route('/member', methods=['GET', 'POST'])
# @login_required
def member():
    return render_template('member.html') # NOQA

