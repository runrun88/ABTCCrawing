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
from decimal import *
import time
from datetime import datetime, date
from datetime import timedelta
import mistune

def get_shGZData():
    sh000001 = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20YcVwDlag={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27000001%27)'
    r = requests.get(sh000001)
    returData = r.text.strip()
    if len(returData) < 2:
        return ""
    startIndex = returData.find('[', 0, len(returData))
    endIndex = returData.find(']', 0, len(returData)) + 1
    midData = returData[startIndex:endIndex]
    data = json.loads(midData)
    # print(data[0]['NEW'])
    hqshGZ = [0, 0, 0, 0, 0]
    hqshGZ[0] = "上证综指"
    jrsp = Decimal(data[0]['NEW']).quantize(Decimal("0.00"))
    hqshGZ[1] = str(jrsp)
    # zdf % 前面数字
    zdf = Decimal(data[0]['CHG']).quantize(Decimal("0.00"))
    hqshGZ[2] = str(zdf)
    zsz = Decimal(data[0]['ZSZ']).quantize(Decimal("0"))
    hqshGZ[3] = str(zsz)
    pe = Decimal(data[0]['SYLAVG']).quantize(Decimal("0.00"))
    hqshGZ[4] = str(pe)
    return hqshGZ


def get_shCJData():
    sh000001 = 'http://push2his.eastmoney.com/api/qt/stock/kline/get?secid=1.000001&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&beg=20200327&end=20220101&_=1585306141156'
    r = requests.get(sh000001)
    returData = r.text

    data2 = json.loads(returData)

    subData = data2['data']

    kline = subData['klines']
    kstr = data2['data']['klines']
    # print(type(kstr))
    shCJData = kstr[0].split(',')
    cjze = (Decimal(shCJData[6]) / 100000000).quantize(Decimal("0.00"))

    # print(cjze)

    # 返回当日成交总额
    return str(cjze)


def get_shenzhenGZData():
    sz399001 = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20oWoofZaK={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399001%27)'
    r = requests.get(sz399001)
    returData = r.text.strip()
    if len(returData) < 2:
        return ""
    startIndex = returData.find('[', 0, len(returData))
    endIndex = returData.find(']', 0, len(returData)) + 1
    midData = returData[startIndex:endIndex]
    data = json.loads(midData)

    # print(data[0]['NEW'])

    hqshenzhenGZ = [0, 0, 0, 0, 0]
    hqshenzhenGZ[0] = "深圳成指"
    jrsp = Decimal(data[0]['NEW']).quantize(Decimal("0.00"))
    zdf = Decimal(data[0]['CHG']).quantize(Decimal("0.00"))
    zsz = Decimal(data[0]['ZSZ']).quantize(Decimal("0"))
    pe = Decimal(data[0]['SYLAVG']).quantize(Decimal("0.00"))

    hqshenzhenGZ[1] = str(jrsp)
    hqshenzhenGZ[2] = str(zdf)
    hqshenzhenGZ[3] = str(zsz)
    hqshenzhenGZ[4] = str(pe)

    return hqshenzhenGZ


def get_shenzhenCJData():
    sz399001 = "http://push2his.eastmoney.com/api/qt/stock/kline/get?secid=0.399001&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&beg=20200321&end=20220101&_=1585306349685"
    r = requests.get(sz399001)
    returData = r.text

    # print(type(returData))
    # print(returData)
    data2 = json.loads(returData)
    # print(type(data2))
    # print(data2['data'])
    subData = data2['data']

    kline = subData['klines']
    kstr = data2['data']['klines']
    # print(type(kstr))
    shenzhenCJData = kstr[0].split(',')

    cjze = (Decimal(shenzhenCJData[6]) / 100000000).quantize(Decimal("0.00"))
    # 返回当日成交总额
    return str(cjze)


def get_zhongxiaoGZData():
    timesp = int(time.time())
    timsp1 = int(timesp / 30000)
    sz399005 = "http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&filter=(MKTCODE=%27399005%27)&rt=" + str(timsp1)
    r = requests.get(sz399005)

    returData = r.text.strip()
    if len(returData) < 2:
        return "No Data"

    data = json.loads(returData)
    #print(data[0]['NEW'])

    hqzhongxiaoGZ = [0, 0, 0, 0, 0]
    hqzhongxiaoGZ[0] = "中小板"
    jrsp = Decimal(data[0]['NEW']).quantize(Decimal("0.00"))
    zdf = Decimal(data[0]['CHG']).quantize(Decimal("0.00"))
    zsz = Decimal(data[0]['ZSZ']).quantize(Decimal("0"))
    pe = Decimal(data[0]['SYLAVG']).quantize(Decimal("0.00"))

    hqzhongxiaoGZ[1] = str(jrsp)
    hqzhongxiaoGZ[2] = str(zdf)
    hqzhongxiaoGZ[3] = str(zsz)
    hqzhongxiaoGZ[4] = str(pe)

    return hqzhongxiaoGZ


def get_zhongxiaoCJData():
    timesp = int(time.time())
    today = date.today() - timedelta(days=1)
    #print(today.strftime('%Y%m%d'))
    sz399005 = "http://push2his.eastmoney.com/api/qt/stock/kline/get?secid=0.399005&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&beg=" + today.strftime(
        '%Y%m%d') + "&end=20220101&_=" + str(timesp)
    r = requests.get(sz399005)
    returData = r.text

    data2 = json.loads(returData)
    subData = data2['data']

    kline = subData['klines']
    if (len(kline) < 1):
        return "Today is weekend"
    kstr = data2['data']['klines']
    zhongxiaoCJData = kstr[0].split(',')

    cjze = (Decimal(zhongxiaoCJData[6]) / 100000000).quantize(Decimal("0.00"))
    # 返回当日成交总额
    return str(cjze)


def get_chuangbanGZData():
    timesp = int(time.time())
    timsp1 = int(timesp / 30000)
    sz399006 = "http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&filter=(MKTCODE=%27399006%27)&rt=" + str(
        timsp1)
    #   sz399006 = "http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=GZFX_SCTJ&token=894050c76af8597a853f5b408b759f5d&st=TDATE&sr=-1&p=1&ps=1&js=var%20uOqCSajO={pages:(tp),data:(x),font:(font)}&filter=(MKTCODE=%27399006%27)&rt=52832426"
    r = requests.get(sz399006)
    returData = r.text.strip()

    returData = r.text.strip()
    if len(returData) < 2:
        return "No Data"

    data = json.loads(returData)
    # print(data[0]['NEW'])

    jrsp = Decimal(data[0]['NEW']).quantize(Decimal("0.00"))
    zdf = Decimal(data[0]['CHG']).quantize(Decimal("0.00"))
    zsz = Decimal(data[0]['ZSZ']).quantize(Decimal("0"))
    pe = Decimal(data[0]['SYLAVG']).quantize(Decimal("0.00"))

    chuanbanGZ = [0, 0, 0, 0, 0]
    chuanbanGZ[0] = "创业板"
    chuanbanGZ[1] = str(jrsp)
    chuanbanGZ[2] = str(zdf)
    chuanbanGZ[3] = str(zsz)
    chuanbanGZ[4] = str(pe)

    return chuanbanGZ


def get_chuanbanCJData():
    timesp = int(time.time())
    today = date.today() - timedelta(days=1)
    # print(today.strftime('%Y%m%d'))

    sz399006 = "http://push2his.eastmoney.com/api/qt/stock/kline/get?secid=0.399006&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&beg=" + today.strftime(
        '%Y%m%d') + "&end=20220101&_=" + str(timesp)
    r = requests.get(sz399006)
    returData = r.text

    # print(type(returData))
    # print(returData)
    data2 = json.loads(returData)
    # print(type(data2))
    # print(data2)
    # print(data2['data'])
    subData = data2['data']

    kline = subData['klines']
    if (len(kline) < 1):
        return "Today is weekend"

    kstr = data2['data']['klines']
    # print(type(kstr))
    chuanbanCJData = kstr[0].split(',')
    cjze = (Decimal(chuanbanCJData[6]) / 100000000).quantize(Decimal("0.00"))
    # 返回当日成交总额
    return str(cjze)


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

    indx = zdf.find('%', 0, len(zdf))

    zdf1 = zdf[0:indx]

    cellist = varStr[0].find_all('div', class_='val')
    btczl = round(float((cellist[2].string).replace(',', '')) / 10000, 2)

    hqBTC[1] = btcprice
    hqBTC[2] = zdf1
    hqBTC[3] = btcZSZ
    hqBTC[4] = btczl
    hqBTC[5] = jye24

    return hqBTC

def investCal():
    # 明天
    nextday = date.today() + timedelta(days=2)
    # 大后天
    nextnextday = date.today() + timedelta(days=4)

    start_time = int(time.mktime(nextday.timetuple()))
    end_time = int(time.mktime(nextnextday.timetuple()))

    event_categorys = ['newstock_onlist', 'newstock_apply', 'CNV', 'FUND', 'BOND', 'STOCK'
        , 'OTHER', 'newbond_apply', 'newbond_onlist', 'diva', 'divhk']
    # 2020-03-27 00:00:00 ==>2020-03-27 23:59:59 currnent:1585311299000

    nowtime = int(time.time())

    for type in event_categorys:
        url = "https://www.jisilu.cn/data/calendar/get_calendar_data/?qtype=" + type + "&start=" + str(start_time) + "&end=" + str(end_time) + "&_=" + str(nowtime)
        # print(url)
        r = requests.get(url)
        returData = r.text.strip()
   #     print(len(returData) )
        if len(returData) < 4:
            continue

        str1 = returData.replace("<br>", " ")
        str2 = str1.replace("\\r\\n", " ")
        data2 = json.loads(str2)
        for obj in data2:
            #       print(obj)
            print(obj["title"], end=" ")
            print(obj["start"], end=" ")
            print(obj["description"])

        return True


def wirteOutput():
    filename = 'a.md'
    output_obj = open(filename, 'w')
    output_obj.write("|  | 今日指數|行情漲跌|交易量|總市值(亿)|市盈率|")
    output_obj.write("\n")
    output_obj.write("| ---- | ---- | ---- |---- |---- |---- |")
    output_obj.write("\n")
    output_obj.close()




if __name__ == "__main__":
    # 设置默认编码格式为utf8
    # reload(sys)
    importlib.reload(sys)

dt = datetime.now()
print(dt)
timeStr = dt.strftime('%H:%M:%S')

timesp = int(time.time())
timsp1 = int(timesp / 30000)

today = date.today()
# print(today.strftime('%Y%m%d'))

#booldata= investCal()


sh_gz = get_shGZData()
sh_cj = get_shCJData()

shanghaiData = [sh_gz[0], sh_gz[1], sh_gz[2], sh_cj, sh_gz[3], sh_gz[4]]
print(shanghaiData)



'''
shenzhen_gz = get_shenzhenGZData()
shenzhen_cj = get_shenzhenCJData()
shenzhenData = [shenzhen_gz[0], shenzhen_gz[1], shenzhen_gz[2], shenzhen_cj, shenzhen_gz[3], shenzhen_gz[4]]
print(shenzhenData)

zhongxiao_gz = get_zhongxiaoGZData()
zhongxiao_cj = get_zhongxiaoCJData()
zhongxiaoData = [zhongxiao_gz[0], zhongxiao_gz[1], zhongxiao_gz[2], zhongxiao_cj, zhongxiao_gz[3], zhongxiao_gz[4]]
print(zhongxiaoData)

chuanban_gz = get_chuangbanGZData()
chuanban_cj = get_chuanbanCJData()
chuangbanData = [chuanban_gz[0], chuanban_gz[1], chuanban_gz[2], chuanban_cj, chuanban_gz[3], chuanban_gz[4]]
print(chuangbanData)

btcData = get_BTCData()
print(btcData)

print(dt)


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
'''
