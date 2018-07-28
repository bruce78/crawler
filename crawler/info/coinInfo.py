import requests
from lxml import html
from lxml.cssselect import CSSSelector


def getCoinInfo(coin):
    url = 'https://www.feixiaohao.com/currencies/'+coin
    ret = requests.get(url)

    tree = html.fromstring(ret.text)

    h24 = tree.xpath('//*[@id="baseInfo"]/div[1]/div[1]/div[3]/div[1]/span/text()')[0]
    l24 = tree.xpath('//*[@id="baseInfo"]/div[1]/div[1]/div[3]/div[2]/span/text()')[0]

    percentage = tree.xpath('//*[@id="baseInfo"]/div[1]/div[2]/div[5]/div/span/text()')[0]
    flowRate = tree.xpath('//*[@id="baseInfo"]/div[1]/div[3]/div[5]/div/span/text()')[0]
    turnoverRate = tree.xpath('//*[@id="baseInfo"]/div[1]/div[4]/div[5]/div/span/text()')[0]

    icoInfo = tree.xpath('/html/body/div[5]/div/div[6]/table')
    info = {}
    if len(icoInfo) > 0:
        sel = CSSSelector('tr td')
        tds = sel(icoInfo[0])
        vals = ["status", "platform", "icoDistribute", "investPercentage", "icoTotal", "icoSupply", "icoStart", "icoStop", "icoOpenPrice", "icoMethod", "icoTarget", "icoVolume", "icoAveragePrice", "icoSuccessCount", "icoSuccessVolume", "characteristic", "security", "law", "area", "consultant", "sellAgentAddress", "blogAddress"]
        for index, td in enumerate(tds):
            if index < len(vals):
                text = "" if td.text is None else td.text
                info[vals[index]] = text

    result = {
        "coin": coin,
        "h24": h24,
        "l24": l24,
        "percentage": percentage,
        "flowRate": flowRate,
        "turnoverRate": turnoverRate,
        "info": str(info)
    }
    return result

# dd = getCoinInfo('eos')
# print(dd)

