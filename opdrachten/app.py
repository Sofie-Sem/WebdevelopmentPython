from flask import Flask, render_template

import datetime
now = datetime.datetime.now()
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/contact')
def contact():
    return("Pietje Puk <br> straat <br> telfoonnummer")

@app.route('/daytime')
def daytime():
    return(now.strftime("%Y-%m-%d <br> %H:%M:%S"  ))

@app.route('/zeghallo/<name>')
def sayhello(name):
    if name == 'Rosa':
        return("Hallo "+name+" Hageman")
    else:
        return('Hallo '+ name)

@app.route('/aftellen/<int:vanaf>')
def aftellen(vanaf):
    ret = ""
    for i in range(vanaf, 0, -1):
        ret = ret + str(i) + "<br>"
    return ret

@app.route('/tafelvan/<int:getal>')
def tafelvan(getal):
    tafel = ""
    for t in range(11):
        tafel_van = (getal * t)
        tafel = tafel + str(getal) + "x" + str(t) + "=" + str(tafel_van) + "<br>"
    return tafel

@app.route('/aantalletters/<woord>')
def aantalletters(woord):
    lengte_woord = len(woord)
    return(str(lengte_woord))

#Koekjes/Dit%20zijn%20lekkere%20koekjes/3,99
@app.route('/prijs/<productnaam>/<omschrijving>/<prijs>')
def prijs(productnaam, omschrijving, prijs):
    ret = productnaam + "<br>" + omschrijving + "<br>" + prijs
    return(ret)

@app.route('/totale/<product>/<int:aantal>/<int:prijs>')
def totale(product, aantal, prijs):
    totaal = aantal * prijs
    ret = "Je hebt " + str(aantal) + " "+ product + " van " + str(prijs) + " euro gekocht. Dat geeft een totale prijs van " + str(totaal) + " euro."
    return(ret)

@app.route('/btw/<product>/<int:totaal>')
def btw(product, totaal):
    ret = "Je koopt het product " + product + " dat geeft een totale btw van " + str(totaal) + " euro."
    return(ret)

@app.route('/totaal/<int:aantal>/<int:btw>/')
def totaal(aantal, btw):
    ret = 'Je koopt ' + str(aantal) + " producten, dat geeft een totale prijs inclusief btw van: "+ str(btw)
    return(ret)

@app.route('/namen/<string:voornaam>/<string:achternaam>')
def namen(voornaam, achternaam):
    return render_template('shop.html', voornaam=voornaam, achternaam=achternaam)

@app.route('/welkom/<naam>/')
def welkom(naam):
    return render_template('shop.html', naam=naam)







app.run(debug=True)
