from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

import datetime
now = datetime.datetime.now()
app = Flask(__name__)
app.config['SECRET_KEY'] = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"

@app.route('/quiz')
def quiz():
    return render_template('test.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        return redirect('/posts')
    return render_template('index.html', title='Log In', form=form)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    straat = StringField('Straat', validators=[DataRequired()])
    huisnummer = StringField('Huisnummer', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    woonplaats = StringField('Woonplaats', validators=[DataRequired()])
    land = StringField('Land', validators=[DataRequired()])
    telefoonnummer = StringField('Telefoonnummer')
    bezorgen = BooleanField('Bezorgen', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

app.run(debug=True)
