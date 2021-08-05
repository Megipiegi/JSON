import json
import csv
from os import sep

with open ('jsonoutput.json')as file:
    data = json.load(file)
fname='jsonresult.csv'
with open (fname, 'w') as file:
    csv_file = csv.writer(file, delimiter='\t')
    csv_file.writerow(['currency'';' 'code'';' 'bid'';' 'ask'])
    # csv_file.writerow(['currency', 'code', 'bid', 'ask'])
    # csv_file.writerow(['currency', ';', 'code',';', 'bid', ';','ask'])
    # csv_file.writerow(['currency', 'code', 'bid', 'ask'])
    for item in data ['rates']:
        # csv_file.writerow([item['currency'], item['code'], item['bid'], item['ask']])
        csv_file.writerow([item['currency'],';',item['code'],';',item['bid'],';',item['ask']])
