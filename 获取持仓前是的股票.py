from typing import Text
import requests
from bs4 import BeautifulSoup
import collections
stock = []
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}
def parse_fun(fun_url):
    resp = requests.get(fun_url, headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    trs = soup.select('#position_shares div table tr')
    for i in range(1, len(trs)):
        name = trs[i].select('td a')[0].get_text()
        stock.append(name)

parse_fun('http://fund.eastmoney.com/007872.html')
print(collections.Counter(stock))