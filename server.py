import os.path
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, validators, EmailField, csrf
from flask_bootstrap import Bootstrap5
from database import user_details

app = Flask(__name__)
bootstrap = Bootstrap5(app)
SECRET_KEY = os.urandom(64)
app.secret_key = SECRET_KEY


class LogIn(FlaskForm):
    user_email = EmailField('Email', [validators.DataRequired(message='Field is empty'),
                                      validators.Length(message='Email must have more than 8 characters', min=8),
                                      validators.Email(message='Invalid email address', granular_message=True)
                                      ])
    password = PasswordField('Password', [validators.DataRequired(message='Field is empty'),
                                          validators.Length(message='Password must have at least 8 characters', min=8),
                                          ])
    submit = SubmitField('Log In', [validators.DataRequired('Submit credentials')])


@app.route('/')
def home():
    form = LogIn()
    return render_template('login.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LogIn()
    form.validate_on_submit()
    if form.validate_on_submit():
        for x in user_details:
            if request.form['user_email'] in user_details[x]['user_email']:
                if user_details[x]['password'] == request.form['password']:
                    print('We got here!')
                    return render_template('success.html')
        return render_template('denied.html')

    return render_template('login.html', form=form)


@app.route('/success')
def welcome():
    return 'Welcome back user!'


if __name__ == "__main__":
    app.run(debug=True)
