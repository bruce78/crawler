import requests
from crawler.trend import *

baseUrl = 'http://localhost:5000'


def saveDayData(coin):
    try:
        url = baseUrl+'/hisdata'
        data = fetchDayData(coin)
        json = {'type': 'day', 'coin': coin, 'data': data, 'step': 300}
        ret = requests.post(url, data=json)
        return ret.status_code
    except:
        return -1


def saveWeekData(coin):
    url = baseUrl + '/hisdata'
    data = fetchWeekData(coin)
    json = {'type': 'week', 'coin': coin, 'data': data, 'step': 300}
    ret = requests.post(url, data=json)
    return ret.status_code


def saveMonthData(coin):
    url = baseUrl + '/hisdata'
    data = fetchMonthData(coin)
    json = {'type': 'month', 'coin': coin, 'data': data, 'step': 3600}
    ret = requests.post(url, data=json)
    return ret.status_code


def saveMonth3Data(coin):
    url = baseUrl + '/hisdata'
    data = fetch3MonthsData(coin)
    json = {'type': 'month3', 'coin': coin, 'data': data, 'step': 7200}
    ret = requests.post(url, data=json)
    return ret.status_code


def saveYearData(coin):
    url = baseUrl + '/hisdata'
    data = fetchYearData(coin)
    json = {'type': 'year', 'coin': coin, 'data': data, 'step': 86400}
    ret = requests.post(url, data=json)
    return ret.status_code


def saveYearFromBeginningData(coin):
    url = baseUrl + '/hisdata'
    data = fetchFromBeginning(coin)
    json = {'type': 'thisyear', 'coin': coin, 'data': data, 'step': 86400}
    ret = requests.post(url, data=json)
    return ret.status_code


def saveAllData(coin):
    url = baseUrl + '/hisdata'
    data = fetchFromBeginning(coin)
    json = {'type': 'all', 'coin': coin, 'data': data, 'step': 172800}
    ret = requests.post(url, data=json)
    return ret.status_code


def updateOnePoint(coin, type):
    url = baseUrl + '/hisdata'
    data = fetchOnePoint(coin)
    json = {'data': data}
    myUrl = url+'/'+coin+'/'+type
    ret = requests.put(myUrl, data=json)
    return ret.status_code


def refreshAllData(coin):
    saveDayData(coin)
    saveWeekData(coin)
    saveMonthData(coin)
    saveMonth3Data(coin)
    saveYearData(coin)
    saveYearFromBeginningData(coin)
    saveAllData(coin)


def saveCoinInfo(info):
    url = baseUrl + '/coininfo'
    ret = requests.post(url, data=info)
    return ret.status_code


def saveExchangeInfo(info):
    url = baseUrl + '/exchangeinfo'
    ret = requests.post(url, data=info)
    return ret.status_code


