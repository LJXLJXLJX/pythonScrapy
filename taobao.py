'''
似乎不是很稳定
可能是淘宝有反爬虫手段？
'''

import requests
import re


def getHTMLText(url): 
    r=requests.get(url,timeout=30)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text
  
      


def parsePage(ilt, html):
  
    plt=re.findall(r'"view_price":"[\d.]*"',html)
    tlt=re.findall(r'"raw_title":".*?"',html)
    for i in range(len(plt)):
        price=eval(plt[i].split(':')[1])
        title=eval(tlt[i].split(':')[1])
        ilt.append([price,title])
   


def printGoodsList(ilt):
    tplt='{:4}\t{:8}\t{:16}'
    print(tplt.format('序号','价格','商品名称'))
    count=0
    for g in ilt:
        count+=1
        print(tplt.format(count,g[0],g[1]))


def main():
    goods = '书包'
    depth = 2
    start_url = r'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + r'&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue

    printGoodsList(infoList)

main()