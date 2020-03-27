# __author__ = 'Fintech'
# -*- coding: utf-8 -*-
import datetime
import sys
import importlib
from bs4 import BeautifulSoup
import re
import requests
import chardet
import json
import csv


def get_subject():
    today = datetime.datetime.now().date()
    subject = "天天基金" % str(today)
    return subject


if __name__ == "__main__":
    # 设置默认编码格式为utf8
    # reload(sys)
    importlib.reload(sys)

    sh000001 = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20YcVwDlag={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27000001%27)&rt=5283200'
    sz399001 = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20oWoofZaK={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399001%27)&rt=52832457'
    sz399005 = "http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20kYClIYAS={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399005%27)&rt=52832425"
    sz399006 = "http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20uOqCSajO={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399006%27)&rt=52832426"

    # 0行是 000001,1行是399001
    hangqing = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    r = requests.get(sh000001)

    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, 'lxml')  # lxml为解析器
    varStr = soup.p.string

    # mcode=json.loads(soup.find('p', {'data': '[]'}).get_text())["MKTCODE"]
    #  pattern = re.compile(r'\[\{.*?\}\]', re.S)
    # pattern = re.compile(r'\[\{^".*?"$\}\]',re.S)
    #  script = pattern.findall(varStr)

    pattern = re.compile(r'[[][{](.*?)[}][]]', re.S)
    script = pattern.findall(varStr)

    todayData = script[0].split(',')

    #   print(todayData[0]) #MKTCODE
    #   print(todayData[1]) #TDATE
    #   print(todayData[2]) #NEW
    #   print(todayData[4])  # change
    #   print(todayData[8])  # 总市值
    #   print(todayData[11])  # PE

    new = todayData[2].split(':')
    change = todayData[4].split(':')
    zsz = todayData[8].split(':')
    pe = todayData[11].split(':')

    newDec = float(eval(new[1]))
    changeDec = float(eval(change[1]))
    zszDec = float(eval(zsz[1]))
    peDec = float(eval(pe[1]))

    hangqing[0][0]="上证综指"
    hangqing[0][1] = round(newDec, 2)
    hangqing[0][2] = "%.2f%%" % (changeDec )
    hangqing[0][3] = round(zszDec, 2)
    hangqing[0][4] = round(peDec, 2)

    r = requests.get(sz399001)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, 'lxml')  # lxml为解析器
    varStr = soup.p.string

    pattern = re.compile(r'[[][{](.*?)[}][]]', re.S)
    script = pattern.findall(varStr)

    todayData = script[0].split(',')
    new = todayData[2].split(':')
    change = todayData[4].split(':')
    zsz = todayData[8].split(':')
    pe = todayData[11].split(':')

    newDec = float(eval(new[1]))
    changeDec = float(eval(change[1]))
    zszDec = float(eval(zsz[1]))
    peDec = float(eval(pe[1]))

    hangqing[1][0] = "深圳成指"
    hangqing[1][1] = round(newDec, 2)
    hangqing[1][2] = "%.2f%%" % (changeDec )
    hangqing[1][3] = round(zszDec, 2)
    hangqing[1][4] = round(peDec, 2)

    r = requests.get(sz399005)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, 'lxml')  # lxml为解析器
    varStr = soup.p.string

    pattern = re.compile(r'[[][{](.*?)[}][]]', re.S)
    script = pattern.findall(varStr)

    todayData = script[0].split(',')
    new = todayData[2].split(':')
    change = todayData[4].split(':')
    zsz = todayData[8].split(':')
    pe = todayData[11].split(':')

    newDec = float(eval(new[1]))
    changeDec = float(eval(change[1]))
    zszDec = float(eval(zsz[1]))
    peDec = float(eval(pe[1]))

    hangqing[2][0] = "中小板"
    hangqing[2][1] = round(newDec, 2)
    hangqing[2][2] = "%.2f%%" % (changeDec )
    hangqing[2][3] = round(zszDec, 2)
    hangqing[2][4] = round(peDec, 2)

    r = requests.get(sz399006)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, 'lxml')  # lxml为解析器
    varStr = soup.p.string

    pattern = re.compile(r'[[][{](.*?)[}][]]', re.S)
    script = pattern.findall(varStr)

    todayData = script[0].split(',')
    new = todayData[2].split(':')
    change = todayData[4].split(':')
    zsz = todayData[8].split(':')
    pe = todayData[11].split(':')

    newDec = float(eval(new[1]))
    changeDec = float(eval(change[1]))
    zszDec = float(eval(zsz[1]))
    peDec = float(eval(pe[1]))

    hangqing[3][0] = "创业板"
    hangqing[3][1] = round(newDec, 2)
    hangqing[3][2] =  "%.2f%%" % (changeDec )
    hangqing[3][3] = round(zszDec, 2)
    hangqing[3][4] = round(peDec, 2)


    btcUrl = "https://www.feixiaohao.com/currencies/bitcoin/"

    # 0行是 000001,1行是399001

    hangqing[4][0]='BTC'

    r = requests.get(btcUrl)


    soup = BeautifulSoup(r.text, 'lxml')  # lxml为解析器
    varStr = soup.find_all('div', class_='priceInfo')

    btclist=varStr[0].find_all('span', class_='convert')
    btcprice =int(float(btclist[0].string))

    btcZSZ=round(float((btclist[2].string).replace(',',''))/100000000,2)

    todayIndex=varStr[0].find_all('div', class_='sub smallfont')
    zdf=todayIndex[0].find('span').string

    cellist=varStr[0].find_all('div',class_='val')
    btczl=round(float((cellist[2].string).replace(',',''))/10000 ,2)

    hangqing[4][1] = btcprice
    hangqing[4][2] = zdf
    hangqing[4][3] = btcZSZ
    hangqing[4][4] = btczl

'''
    f= open('./test.txt', 'w')
    for m in range(4):
        for n in range(4):
            f.write(str(hangqing[m][n]) + " ")
            if(n==3):
                f.write("\n")

    f.close()
'''

dt = datetime.datetime.now()

dtStr = dt.strftime('%Y%m%d')

timeStr=dt.strftime('%H:%M:%S')
print(timeStr)

f = open(dtStr + ".csv", 'w', newline='')
writer = csv.writer(f)
writer.writerow([' ','今日指數', '行情漲跌', '總市值(亿)','市盈率'])

for i in hangqing:
    writer.writerow(i)

writer.writerow(['','','','',''])
writer.writerow(['','','时间：',dtStr,timeStr])
f.close()

#  gz=soup.find("span", id="gz_gsz")
# print(r.encoding)

#   stock_crawler = stock_crawler()
#   email_text = stock_crawler.get_email_text() + "\n"

#    subject = get_subject()
# 发送邮件
#   send_email(subject, email_text)
