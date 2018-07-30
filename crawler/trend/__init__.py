import requests
import datetime
import time
from dateutil.relativedelta import relativedelta


def fetchData(coin, timeParams):
    headers = {
        "Content-type": "application/json",
    }
    ret = requests.get('http://api.feixiaohao.com/coinhisdata/'+coin+'/'+timeParams,headers)
    return ret


# step 5 minutes
def fetchDayData(coin):
    now = datetime.datetime.now()
    toTime = int(round(time.time())) * 1000
    fromTime = toTime - (now.hour*3600+now.minute*60)*1000
    timeParams = str(fromTime)+'/'+str(toTime)
    return fetchData(coin, timeParams)


def fetchByDay(coin, days):
    toTime = int(round(time.time())) * 1000
    fromTime = toTime - (days*24*3600) * 1000
    timeParams = str(fromTime) + '/' + str(toTime)
    return fetchData(coin, timeParams)


def fetchByMonth(coin, months):
    now = datetime.datetime.now()
    last = now - relativedelta(months=months)

    days = int((now.timestamp()-last.timestamp())/3600/24)
    return fetchByDay(coin, days)


# step 5 minutes
def fetchWeekData(coin):
    return fetchByDay(coin, 7)


# step 1 hour
def fetchMonthData(coin):
    return fetchByMonth(coin, 1)


# step 2 hours
def fetch3MonthsData(coin):
    return fetchByMonth(coin, 3)


# step 1 day
def fetchYearData(coin):
    return fetchByMonth(coin, 12)


# step 1 day
def fetchFromYearBeginning(coin):
    today = datetime.datetime.now()
    days = (today - datetime.datetime(today.year, 1, 1)).days + 1

    toTime = int(round(time.time())) * 1000
    fromTime = toTime - (days*24*3600+today.hour*3600+today.minute*60+today.second) * 1000
    timeParams = str(fromTime) + '/' + str(toTime)
    return fetchData(coin, timeParams)


def fetchFromBeginning(coin):
    today = datetime.datetime.now()
    months = today.month+24
    return fetchByMonth(coin, months)


# span time is 1 min
def fetchOnePoint(coin):
    toTime = int(round(time.time())) * 1000
    fromTime = toTime - (1 * 60) * 1000
    timeParams = str(fromTime) + '/' + str(toTime)
    return fetchData(coin, timeParams)
