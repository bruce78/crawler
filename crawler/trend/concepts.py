import requests
from lxml import html
from lxml.cssselect import CSSSelector
import threading
import time

class CrawlerThread(threading.Thread):
    binarySemaphore = threading.Semaphore(1)

    def __init__(self, binarySemaphore, callback, page, results):
        self.binarySemaphore = binarySemaphore

        self.callback = callback
        self.page = page
        self.results = results
        self.threadId = hash(self)
        threading.Thread.__init__(self)

    def run(self):
        # self.binarySemaphore.acquire()  # wait if another thread has acquired and not yet released binary semaphore
        self.results.append(self.callback(self.page))
        # self.binarySemaphore.release()


def pageSize():
    url = 'https://www.feixiaohao.com/'
    ret = requests.get(url)

    tree = html.fromstring(ret.text)
    val = tree.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/a[8]/text()')[0]
    return int(val)


def getPageCoins(num):
    url = 'https://www.feixiaohao.com'
    if num != 1:
        url = url+'/list_'+str(num)+'.html'
    ret = requests.get(url)
    tree = html.fromstring(ret.text)
    sel = CSSSelector('table.new-coin-list tbody tr')
    results = sel(tree)

    sel2 = CSSSelector('td:nth-child(2) > a')

    list2 = []
    for result in results:
        res = sel2(result)
        if len(res) > 0:
            href = res[0].get('href')
            length = len('/currencies/')
            coin = href[length:len(href)-1]
            list2.append(coin)
    return list2


def getAllCoins():
    pages = pageSize()
    coins = []
    for page in range(1, pages+1):
        list2 = getPageCoins(page)
        coins.append(list2)

    return coins


# start = time.process_time()
# coins2 = getAllCoins()
# print(coins2)
# print(time.process_time())

# def hello():
#     print("hello, world")
#
# t = Timer(3.0, hello)
# t.start()

