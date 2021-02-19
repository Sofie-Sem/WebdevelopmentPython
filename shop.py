from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

import datetime
now = datetime.datetime.now()
app = Flask(__name__)
app.config['SECRET_KEY'] = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"

class Prijzen():
    film1 = 7.99 #The_Maze_Runner
    film2 = 11.99 #Beauty_and_the_Beast
    film3 = 11.99 #Fantastic_Beasts
    film4 = 5.99 #The_Mortal_Instruments
    film5 = 10.99 #Harry_Potter
    film6 = 12.99 #Lord_of_the_Rings
    film7 = 9.99 #Narnia
    film8 = 46.49 #The_never_ending_story

@app.route('/webshop')
def webshop():
    return render_template('index.html')

@app.route('/webshop/fantasy')
def fantasy():
    prijzen=Prijzen()
    return render_template('Fantasy.html', prijzen=prijzen)

@app.route('/webshop/sci-fi')
def scifi():
    return render_template('Sci-Fi.html')

@app.route('/webshop/bestelpagina/<film>/', methods=['GET', 'POST'])
def bestelpagina(film):
    form=LoginForm()
    if form.validate_on_submit():
        return render_template('bedankt.html')
    prijzen=Prijzen()
    return render_template('bestelpagina.html', film=film, prijzen=prijzen, title='Log In', form=form)

@app.route('/webshop/bedankt/')
def bedankt():
    return render_template('bedankt.html')

@app.route('/webshop/informatie/<nummer>/<film>/<prijs>/<genre>/<informatie>')
def informatie(nummer, film, prijs, genre,  informatie):
    prijzen=Prijzen()
    return render_template('informatie.html', prijzen=prijzen, nummer=nummer, film=film, prijs=prijs, genre=genre, info=informatie)

class LoginForm(FlaskForm):
    username = StringField('Naam', validators=[DataRequired()])
    straat = StringField('Straat', validators=[DataRequired()])
    huisnummer = StringField('Huisnummer', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    woonplaats = StringField('Woonplaats', validators=[DataRequired()])
    land = StringField('Land', validators=[DataRequired()])
    telefoonnummer = StringField('Telefoonnummer')
    bezorgen = BooleanField('Bezorgen')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


app.run(debug=True)
