import requests
import json

from flask import Flask, render_template, request, redirect

response = requests.get('https://api.nbp.pl/api/exchangerates/tables/C?format=json')

content = response.content
data = json.loads(content)

for x in (data[0]['rates']):
    if (x['code'] == 'USD'):
        print(x['bid'])
        usdValue = x['bid']
    elif (x['code'] == 'AUD'):
        print(x['bid'])
        audValue = x['bid']
    elif (x['code'] == 'EUR'):
        print(x['bid'])
        eurValue = x['bid']
    elif (x['code'] == 'CAD'):
        print(x['bid'])
        cadValue = x['bid']

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
    currencyCode=request.form.get('currencyCode')
    currencyAmount=request.form.get('currencyAmount')
    if (currencyCode == 'USD'):
        currencyValue = usdValue
    elif (currencyCode == 'AUD'):
        currencyValue = audValue
    elif (currencyCode == 'EUR'):
        currencyValue = eurValue
    elif (currencyCode == 'CAD'):
        currencyValue = cadValue
    else:
        currencyValue = 0
    totalValuePln = float(currencyValue) * float(currencyAmount)
    print(totalValuePln)

    title = "Kalkulator"
    return render_template('result.html', title=title, currencyCode=currencyCode, currencyAmount=currencyAmount, totalValuePln=totalValuePln)
