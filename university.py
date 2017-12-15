import requests
import bs4
from bs4 import BeautifulSoup
import os

def getHTMLText(url):
    try:
        kv={'user_agent':'Mozilla/5.0'}
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            tds[1]=tds[1]('div')[0]
            ulist.append([tds[0].contents[0],tds[1].string,tds[2].string,tds[3].string,tds[4].string,tds[5].string,tds[6].string,tds[7].string,tds[8].string,tds[9].string,tds[10].string,tds[11].string,tds[12].string])


def printUnivList(ulist,num):
    tplt='{:^5}\t{:^15}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    print(tplt.format('排名','学校','省市','总分','生源质量','就业率','论文数量','论文质量','高被引论文篇数','高被引学者','企业科研经费','技术转让收入','留学生比例',chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],chr(12288)))

    print('Suc'+str(num))

def main():
    uinfo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20) #20univ

main()