from typing import Text
import requests
from lxml import etree
import datetime
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}
def parse_list(page_url):
    pass

def getStockCodeList():
    today = datetime.date.today()
    str_time = today.strftime('%Y%m%d')
    page_url = f"http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;s6yzf;pn50;ddesc;qsd{str_time};qed{str_time};qdii;zq;gg;gzbd;gzfs;bbzt;sfbb"
    resp = requests.get(page_url, headers)
    resp.encoding = 'utf-8'
    text = resp.text
    parser = etree.HTML(text)
    print(text)

getStockCodeList()