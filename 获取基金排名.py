from logging import error
from os import write
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import requests
from bs4 import BeautifulSoup
import collections
import pandas as pd
import datetime


stock = []
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}
def parse_fun(fun_url):
    resp = requests.get(fun_url, headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    trs = soup.select('#position_shares div table tr')
    print(len(trs))
    if(len(trs) > 2):
        for i in range(1, len(trs)):
            name = trs[i].select('td a')[0].get_text()
            stock.append(name)
    else:
        print('该基金数据错误:' + fun_url)

#股票统计排序规则，指定第二个元素排序
def takeSecond(elem):
    return elem[1]
_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
# url = 'http://fund.eastmoney.com/data/fundranking.html#tgp;c0;r;szzf;pn50;dasc;qsd'+_date+';qed'+_date+';qdii;zq;gg;gzbd;gzfs;bbzt;sfbb'  #近一周跌幅基金排名排名
url = 'http://fund.eastmoney.com/data/fundranking.html#tgp;c0;r;s1yzf;pn50;dasc;qsd'+_date+';qed'+_date+';qdii;zq;gg;gzbd;gzfs;bbzt;sfbb'  #近一个月跌幅基金排名
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()
driver.get(url)
data = []
print('-----------------开始爬虫操作-----------------')

element = driver.find_element_by_xpath('//*[@id="showall"]')               #不分页
ActionChains(driver).click(element).perform()
time.sleep(6)
demo = []
fun_names = []
demo.append('序号')
demo.append('基金编号')
demo.append('基金名称')
demo.append('日期')
demo.append('单位净值')
demo.append('累计净值')
demo.append('日增长')
demo.append('周增长')
demo.append('月增长')
demo.append('3个月增长')
demo.append('6个月增长')
demo.append('年增长')
demo.append('两年增长')
demo.append('三年增长')
demo.append('总体增长')
demo.append('购买费率')
# data.append(demo)
i = 0
while len(data) < 21:
    print(len(data))
    i += 1
    try:
        num = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[3]').text
        xuhao = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[2]').text
        
        name = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[4]').text
        date = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[5]').text
        danweijingzhi = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[6]').text
        leijijingzhi = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[7]').text
        day_grow = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[8]').text
        week_grow = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[9]').text
        month_grow = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[10]').text
        three_month_grow = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[11]').text
        six_month_grow = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[12]').text
        year_grow = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[13]').text
        two_year_grow = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[14]').text
        three_year_grow = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[15]').text
        all_grow = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[17]').text
        fee = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[19]').text
        print(name)
        parse_fun(f"http://fund.eastmoney.com/{num}.html")
        
        temp = []
        temp.append(xuhao)
        temp.append(num)
        temp.append(name)
        temp.append(date)
        temp.append(danweijingzhi)
        temp.append(leijijingzhi)
        temp.append(day_grow)
        temp.append(week_grow)
        temp.append(month_grow)
        temp.append(three_month_grow)
        temp.append(six_month_grow)
        temp.append(year_grow)
        temp.append(two_year_grow)
        temp.append(three_year_grow)
        temp.append(all_grow)
        temp.append(fee)
        
        
        print(temp)
        
        if(name not in fun_names):
            data.append(temp)
            fun_names.append(name)
            
    except BaseException as a:
        # print('找不到元素，爬取结束')
        print(a)
        # i = i-1
        continue    #若因为反爬虫爬取失败，则继续当前轮次的爬取
    
    print('当前正在爬取第'+str(i)+'条')
 
stock_count = collections.Counter(stock)
stock_count_arr = []
for i in stock_count:
    arr = []
    arr.append(i)
    arr.append(stock_count[i])
    stock_count_arr.append(arr)
stock_count_arr.sort(key=takeSecond, reverse=True)

data1 = pd.DataFrame(data, columns=demo)
data2 = pd.DataFrame(stock_count_arr, columns=['股票名称', '基金数量'])
with pd.ExcelWriter(_date+'股票基金持仓统计.xlsx') as writer:
    data1.to_excel(writer, sheet_name='股票型基金业绩排名前20名', index=False)
    data2.to_excel(writer, sheet_name='业绩前20名基金持仓统计', index=False)