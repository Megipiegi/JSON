import requests
import json

from flask import Flask, render_template, request, redirect

response = requests.get('https://api.nbp.pl/api/exchangerates/tables/C?format=json')

content = response.content
data = json.loads(content)


dict_rates = {}
for x in (data[0]['rates']):
    dict_rates[x['code']]=x['bid']

app = Flask(__name__)

@app.route ('/message', methods = ['GET', 'POST'])
def message ():
    if request.method == 'GET':
        print('We received GET')
        return render_template ('walutomat.html')
    elif request.method == 'POST':
        print ('We received POST')
        print (request.form)
        return redirect ('/result.html')

@app.route ('/result', methods = ['POST'])
def form ():
    currency_code=request.form.get('currency_code')
    currency_amount=request.form.get('currency_amount')

    total_value_pln = float(dict_rates[currency_code]) * float(currency_amount)
    total_value_pln = round(total_value_pln, 2)
    print(total_value_pln)
    

    title = "Kalkulator"
    return render_template('result.html', title=title, currency_code=currency_code, currency_amount=currency_amount, total_value_pln=total_value_pln)
