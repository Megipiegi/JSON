import json
import csv
with open ('jsonoutput.json')as file:
    data = json.load(file)
fname='jsonresult.csv'
with open (fname, 'w') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(['currency', 'code', 'bid', 'ask'])
    for item in data ['rates']:
        csv_file.writerow([item['currency'], item['code'], item['bid'], item['ask']])