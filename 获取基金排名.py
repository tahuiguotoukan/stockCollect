# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

url = 'http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;s6yzf;pn50;ddesc;qsd20200730;qed20210730;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb'
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()
driver.get(url)
data = []
print('-----------------开始爬虫操作-----------------')
time.sleep(3)
element = driver.find_element_by_xpath('//*[@id="showall"]')               #不分页
ActionChains(driver).click(element).perform()
time.sleep(6)
demo = []
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
data.append(demo)
for i in range(1,11):
    try:
        xuhao = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[2]').text
        num = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr[' + str(i) + ']/td[3]').text
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
        data.append(temp)
    except :
        print('找不到元素，爬取结束')
        i = i-1
        continue    #若因为反爬虫爬取失败，则继续当前轮次的爬取
    print('当前正在爬取第'+str(i)+'条')


with open(r'E:/dataset.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)
#print(xpath)