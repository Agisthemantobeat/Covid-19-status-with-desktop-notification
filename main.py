import time

from plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:/desktop notification system corona/icon.ico",
        timeout=10
    )
    # app_icon doesn't supports png now. ico format is the best supported one.


def getdata(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    # notifyMe('APOORV', 'Lets stop the spread of this coronavirus together')
    myhtmldata = getdata('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(myhtmldata, 'html.parser')
    # print(soup.prettify())  # BEATUFIES THE DATA
    mydata = ""
    states = ['Chandigarh', 'Punjab', 'Uttar Pradesh', 'Uttarakhand']
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        mydata += tr.get_text()
    mydata = mydata[1:]
    itemlist = (mydata.split('\n\n'))
    for item in itemlist[0:35]:
        datalist = (item.split('\n'))
        if datalist[1] in states:
            print(datalist)
            nTitle = 'Cases of Covid 19'
            nText = f"States : {datalist[1]}\nIndian : {datalist[2]}\nForeign : {datalist[3]}\nCured : {datalist[4]}\nDeaths : {datalist[5]} "
            notifyMe(nTitle,nText)
            time.sleep(2)