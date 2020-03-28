# __author__ = 'Fintech'
# -*- coding: utf-8 -*-
import csv
import datetime
import importlib
import json
import re
import sys

import chardet
import requests
from bs4 import BeautifulSoup


def get_shGZData():
    sh000001 = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20YcVwDlag={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27000001%27)'
    r = requests.get(sh000001)
    returData = r.text.strip()
    # if len(returData) > 2:
    print(type(returData))
    print(returData)
    startIndex = returData.find('[', 0, len(returData))
    endIndex = returData.find(']', 0, len(returData)) + 1
    midData = returData[startIndex:endIndex]
    data = json.loads(midData)
    print(type(data))
    print(data)

    print(data[0]['NEW'])

    hqshGZ = [0, 0, 0, 0, 0]
    hqshGZ[0] = "上证综指"
    hqshGZ[1] = data[0]['NEW']
    hqshGZ[2] = data[0]['CHG']
    hqshGZ[3] = data[0]['ZSZ']
    hqshGZ[4] = data[0]['SYLAVG']

    return hqshGZ

def get_shCJData():
    sh000001 = 'http://push2his.eastmoney.com/api/qt/stock/kline/get?secid=1.000001&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&beg=20200327&end=20220101&_=1585306141156'
    r = requests.get(sh000001)
    returData = r.text

    # print(type(returData))
    # print(returData)
    data2 = json.loads(returData)
    # print(type(data2))
    print(data2)
    print(data2['data'])
    subData = data2['data']

    kline = subData['klines']
    kstr = data2['data']['klines']
    print(type(kstr))
    shCJData = kstr[0].split(',')
    print(shCJData)
    print(shCJData[0])
    print(shCJData[1])

    #返回当日成交总额
    return lastData[6]

def get_shenzhenGZData():
    sz399001 = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20oWoofZaK={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399001%27)'
    r = requests.get(sz399001)
    returData = r.text.strip()
    # if len(returData) > 2:
    print(type(returData))
    print(returData)
    startIndex = returData.find('[', 0, len(returData))
    endIndex = returData.find(']', 0, len(returData)) + 1
    midData = returData[startIndex:endIndex]
    data = json.loads(midData)

    print(data[0]['NEW'])

    hqshenzhenGZ = [0, 0, 0, 0, 0]
    hqshenzhenGZ[0] = "深圳成指"
    hqshenzhenGZ[1] = data[0]['NEW']
    hqshenzhenGZ[2] = data[0]['CHG']
    hqshenzhenGZ[3] = data[0]['ZSZ']
    hqshenzhenGZ[4] = data[0]['SYLAVG']

    return hqshenzhenGZ

def get_shenzhenCJData():
    sz399001 ="http://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery112401635144818190688_1585306349667&secid=0.399001&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&beg=20200321&end=20220101&_=1585306349685"
    r = requests.get(sz399001)
    returData = r.text

    # print(type(returData))
    # print(returData)
    data2 = json.loads(returData)
    # print(type(data2))
    print(data2)
    print(data2['data'])
    subData = data2['data']

    kline = subData['klines']
    kstr = data2['data']['klines']
    print(type(kstr))
    shenzhenCJData = kstr[0].split(',')
    print(shenzhenCJData)
    print(shenzhenCJData[0])
    print(shenzhenCJData[1])

    #返回当日成交总额
    return shenzhenCJData[6]



def get_zhongxiaoGZData():
    sz399005 = "http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20kYClIYAS={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399005%27)&rt=52832425"
    r = requests.get(sz399005)
    returData = r.text.strip()
    # if len(returData) > 2:
    print(type(returData))
    print(returData)
    startIndex = returData.find('[', 0, len(returData))
    endIndex = returData.find(']', 0, len(returData)) + 1
    midData = returData[startIndex:endIndex]
    data = json.loads(midData)

    print(data[0]['NEW'])

    hqzhongxiaoGZ= [0, 0, 0, 0, 0]
    hqzhongxiaoGZ[0] = "中小板"
    hqzhongxiaoGZ[1] = data[0]['NEW']
    hqzhongxiaoGZ[2] = data[0]['CHG']
    hqzhongxiaoGZ[3] = data[0]['ZSZ']
    hqzhongxiaoGZ[4] = data[0]['SYLAVG']

    return hqzhongxiaoGZ

def get_zhongxiaoCJData():
    sz399005 = "http://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery112401635144818190688_1585306349667&secid=0.399005&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&beg=20200321&end=20220101&_=1585306349685"
    r = requests.get(sz399005)
    returData = r.text

    # print(type(returData))
    # print(returData)
    data2 = json.loads(returData)
    # print(type(data2))
    print(data2)
    print(data2['data'])
    subData = data2['data']

    kline = subData['klines']
    kstr = data2['data']['klines']
    print(type(kstr))
    zhongxiaoCJData = kstr[0].split(',')
    print(zhongxiaoCJData)
    print(zhongxiaoCJData[0])
    print(zhongxiaoCJData[1])

    #返回当日成交总额
    return zhongxiaoCJData[6]



def get_chuangbanGZData():
    sz399006 = "http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20uOqCSajO={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399006%27)&rt=52832426"
    r = requests.get(sz399005)
    returData = r.text.strip()
    # if len(returData) > 2:
    print(type(returData))
    print(returData)
    startIndex = returData.find('[', 0, len(returData))
    endIndex = returData.find(']', 0, len(returData)) + 1
    midData = returData[startIndex:endIndex]
    data = json.loads(midData)

    print(data[0]['NEW'])

    chuanbanGZ= [0, 0, 0, 0, 0]
    chuanbanGZ[0] = "创业板"
    chuanbanGZ[1] = data[0]['NEW']
    chuanbanGZ[2] = data[0]['CHG']
    chuanbanGZ[3] = data[0]['ZSZ']
    chuanbanGZ[4] = data[0]['SYLAVG']

    return chuanbanGZ

def get_chuanbanCJData():
    sz399006 = "http://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery112401635144818190688_1585306349667&secid=0.399006&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&beg=20200321&end=20220101&_=1585306349685"
    r = requests.get(sz399006)
    returData = r.text

    # print(type(returData))
    # print(returData)
    data2 = json.loads(returData)
    # print(type(data2))
    print(data2)
    print(data2['data'])
    subData = data2['data']

    kline = subData['klines']
    kstr = data2['data']['klines']
    print(type(kstr))
    chuanbanCJData = kstr[0].split(',')
    print(chuanbanCJData)
    print(chuanbanCJData[0])
    print(chuanbanCJData[1])

    #返回当日成交总额
    return chuanbanCJData[6]

def get_BTCData():
    btcUrl = "https://www.feixiaohao.com/currencies/bitcoin/"

    # 0行是 000001,1行是399001
    hqBTC = [0, 0, 0, 0, 0, 0]
    hqBTC[0] = 'BTC'

    r = requests.get(btcUrl)

    soup = BeautifulSoup(r.text, 'lxml')  # lxml为解析器
    varStr = soup.find_all('div', class_='priceInfo')

    btclist = varStr[0].find_all('span', class_='convert')
    btcprice = int(float(btclist[0].string))

    jye24 = float((btclist[3].string).replace(',', '')) / 100000000
    jye24 = round(jye24, 2)

    btcZSZ = round(float((btclist[2].string).replace(',', '')) / 100000000, 2)

    todayIndex = varStr[0].find_all('div', class_='sub smallfont')
    zdf = todayIndex[0].find('span').string

    cellist = varStr[0].find_all('div', class_='val')
    btczl = round(float((cellist[2].string).replace(',', '')) / 10000, 2)



    hqBTC[1] = btcprice
    hqBTC[2] = zdf
    hqBTC[3] = btcZSZ
    hqBTC[4] = btczl
    hqBTC[5] = jye24

    return  hqBTC


if __name__ == "__main__":
    # 设置默认编码格式为utf8
    # reload(sys)
    importlib.reload(sys)
'''
    sh000001 = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20YcVwDlag={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27000001%27)&rt=5283200'
    sz399001 = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20oWoofZaK={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399001%27)&rt=52832457'
    sz399005 = "http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20kYClIYAS={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399005%27)&rt=52832425"
    sz399006 = "http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20uOqCSajO={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399006%27)&rt=52832426"

    # 0行是 000001,1行是399001
    hangqing = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    r = requests.get(sh000001)
    returData = r.text.strip()
    #if len(returData) > 2:
    print(type(returData))
    print(returData)
    startIndex=returData.find('[', 0, len(returData))
    endIndex=returData.find(']', 0, len(returData))+1
    midData=returData[startIndex:endIndex]
    data = json.loads(midData)
    print(type(data))
    print(data)

    print(data[0]['NEW'])

    hq000001 = [0, 0, 0, 0, 0]
    hq000001[0] = "上证综指"
    hangqing[1] = data[0]['NEW']
    hangqing[2] = data[0]['CHG']
    hangqing[3] = data[0]['ZSZ']
    hangqing[4] = data[0]['SYLAVG']
'''


zs001 = "http://quote.eastmoney.com/zs000001.html"

r = requests.get(zs001)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, 'lxml')  # lxml为解析器
trs = soup.find_all('table', class_='yfw')
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

hangqing[0][0] = "上证综指"
hangqing[0][1] = round(newDec, 2)
hangqing[0][2] = "%.2f%%" % (changeDec)
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
hangqing[1][2] = "%.2f%%" % (changeDec)
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
hangqing[2][2] = "%.2f%%" % (changeDec)
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
hangqing[3][2] = "%.2f%%" % (changeDec)
hangqing[3][3] = round(zszDec, 2)
hangqing[3][4] = round(peDec, 2)

btcUrl = "https://www.feixiaohao.com/currencies/bitcoin/"

# 0行是 000001,1行是399001

hangqing[4][0] = 'BTC'

r = requests.get(btcUrl)

soup = BeautifulSoup(r.text, 'lxml')  # lxml为解析器
varStr = soup.find_all('div', class_='priceInfo')

btclist = varStr[0].find_all('span', class_='convert')
btcprice = int(float(btclist[0].string))

btcZSZ = round(float((btclist[2].string).replace(',', '')) / 100000000, 2)

todayIndex = varStr[0].find_all('div', class_='sub smallfont')
zdf = todayIndex[0].find('span').string

cellist = varStr[0].find_all('div', class_='val')
btczl = round(float((cellist[2].string).replace(',', '')) / 10000, 2)

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

timeStr = dt.strftime('%H:%M:%S')
print(timeStr)

f = open(dtStr + ".csv", 'w', newline='')
writer = csv.writer(f)
writer.writerow([' ', '今日指數', '行情漲跌', '總市值(亿)', '市盈率'])

for i in hangqing:
    writer.writerow(i)

writer.writerow(['', '', '', '', ''])
writer.writerow(['', '', '时间：', dtStr, timeStr])
f.close()

#  gz=soup.find("span", id="gz_gsz")
# print(r.encoding)

#   stock_crawler = stock_crawler()
#   email_text = stock_crawler.get_email_text() + "\n"

#    subject = get_subject()
# 发送邮件
#   send_email(subject, email_text)
