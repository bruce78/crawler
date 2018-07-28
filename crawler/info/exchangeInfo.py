import requests
from lxml import html
from lxml.cssselect import CSSSelector


def pageSize():
    url = 'https://www.feixiaohao.com/exchange'
    ret = requests.get(url)

    tree = html.fromstring(ret.text)
    val = tree.xpath('/html/body/div[5]/div/div[1]/div[2]/div[6]/a[7]/text()')[0]
    return int(val)


def getPageInfos(num):
    url = 'https://www.feixiaohao.com/exchange'
    if num > 1:
        url = url + '/list_' + str(num) + '.html'

    ret = requests.get(url)

    tree = html.fromstring(ret.text)
    trs = tree.xpath('/html/body/div[5]/div/div[1]/div[3]/table/tbody/tr')
    infos = []
    for tr in trs:
        info = {}
        tradeTypes = []
        sel = CSSSelector('td a')
        tds = sel(tr)
        for index, td in enumerate(tds):
            if td.text is not None:
                if index == 1:
                    info['h24Volume'] = td.text
                elif index == 2:
                    info['marketNum'] = td.text
                elif index == 3:
                    info['country'] = td.text

                if len(td.cssselect('a img')) > 0:
                    img = td.cssselect('a img')[0]
                    info['icon'] = img.get('src')
                    href = td.cssselect('a')[0].get('href')
                    info['code'] = href[10:len(href)-1]

            aElm = td.cssselect('a')
            if len(aElm) > 0:

                for elm in aElm:
                    href = elm.get('href')
                    pos = href.find('type=')
                    if pos != -1:
                        tradeTypes.append(href[16:])

        info['tradeTypes'] = ','.join(tradeTypes)
        infos.append(info)

    for info in infos:
        setExInfo(info)
    return infos


def setExInfo(info):
    url = 'https://www.feixiaohao.com/exchange/'+info['code']
    ret = requests.get(url)
    tree = html.fromstring(ret.text)
    info['name'] = tree.xpath('/html/body/div[4]/div/div[1]/div/div/div[2]/div[1]/h1/text()')
    info['homeLink'] = tree.xpath('/html/body/div[4]/div/div[1]/div/div/div[2]/div[4]/span[1]/a/text()')

    elms = tree.xpath('/html/body/div[4]/div/div[2]/div[2]/div[2]/section/p/text()')
    contents = []
    for elm in elms:
        contents.append('<p>')
        contents.append(str(elm))
        contents.append('</p>')
    info['description'] = ''.join(contents)


def getExchangeInfos():
    size = pageSize()
    infos = []

    for page in range(1, size+1):
        list2 = getPageInfos(page)
        infos.extend(list2)

    return infos

# print(len(getInfos()))