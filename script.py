import csv

import requests
import os
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
LIMIT = 1000

url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'
response = requests.get(url)

tickers = []
data = response.json()

#print(data['next_url'])
#print(data.keys())

for ticker in data['results']:
 tickers.append(ticker)

# while 'next_url' in data:
#  print('requesting next page',data['next_url'])
#  response = requests.get(data['next_url'] + f'&apikey={POLYGON_API_KEY}')
#  data = response.json()
#  print(data)
#  for ticker in data['results']:
#   tickers.append(ticker)

print(len(tickers))

example_ticker = {'ticker': 'BBAG',
'name': 'JPMorgan BetaBuilders U.S. Aggregate Bond ETF',
'market': 'stocks',
'locale': 'us',
'primary_exchange': 'ARCX',
'type': 'ETF',
'active': True,
'currency_name': 'usd',
'cik': '0001485894',
'composite_figi': 'BBG00MSHTGF0',
'share_class_figi': 'BBG00MSHTH59',
'last_updated_utc': '2025-09-14T06:09:45.85174312Z'}

fieldnames = list(example_ticker.keys())
output_csv = 'tickets.csv'
with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
 writer = csv.DictWriter(f,fieldnames=fieldnames)
 writer.writeheader()
 for t in tickers:
  row = {key: t.get(key,'')for key in fieldnames}
  writer.writerow(row)
  #breakpoint()
 print(f'Wrote{len(tickers)}rows to {output_csv}')

