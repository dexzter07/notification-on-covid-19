from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\dhira\\Desktop\\notification\\corona.ico",
        timeout=10
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    # notifyMe("Dexzter", "Lets stop the spread of covid-19")
    while True:

        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[7].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = (myDataStr.split("\n\n"))

        states = ["Delhi", "Bihar", "West Bengal"]
        for item in itemList[0:24]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of COVID-19'
                nText = f"{dataList[1]}\n Total Cases: {int(dataList[2]) + int(dataList[3])}\n Cured: {dataList[4]} Deaths: {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)
