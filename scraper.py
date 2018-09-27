# i am not liable for any damage 
# use it at your own risk !!
# its against Etherscan's TOS 
# your ip might get ban for requesting too many times

import csv
import sys
import datetime
import requests
from time import sleep
from bs4 import BeautifulSoup

def scraper(num_pages=1, req_delay=0.1):
  timestamp = datetime.datetime.now().strftime ("%Y%m%d_%H%M%S")
  
  print("%d pages to parse with delay of %d seconds between each page" % (num_pages, req_delay))
  api_url = "https://etherscan.io/contractsVerified/"
  
  with open('VerifiedContracts-'+timestamp+'.csv', 'w') as csvfile:
    fieldnames = ['addr', 'contract_name', 'compiler', 'balance', 'tx_count', 'date_verified']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, num_pages+1):
      url = api_url + str(i) + str('?ps=100')
      sleep(req_delay)
      response = requests.get(url)
      print("URL: %s, Status: %s" % (url, response.status_code))

      content = response.content
      soup = BeautifulSoup(content, 'html.parser')

      for row in soup.select('table.table-hover tbody tr'):
        cells = row.findAll('td')
        cells = map(lambda x: x.text, cells)
        addr, contract_name, compiler, balance, tx_count, settings, date_verified = cells
        writer.writerow({
          'addr': addr,
          'contract_name': contract_name,
          'compiler': compiler,
          'balance': balance,
          'tx_count': tx_count,
          'date_verified': date_verified,
        })

def main():
  if len(sys.argv) > 2:
    scraper(int(sys.argv[1]), int(sys.argv[2]))
  elif len(sys.argv) == 2:
    scraper(int(sys.argv[1]))
  else:
    scraper()

if __name__ == "__main__":
  main()
