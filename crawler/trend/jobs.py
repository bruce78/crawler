from crawler.trend.services import updateOnePoint, refreshAllData, saveCoinInfo, saveExchangeInfo
from apscheduler.schedulers.blocking import BlockingScheduler

from crawler.trend.concepts import getAllCoins
from crawler.info.coinInfo import getCoinInfo
from crawler.info.exchangeInfo import getExchangeInfos

coins = getAllCoins()


def dayWeekJob():
    for oneList in coins:
        for coin in oneList:
            updateOnePoint(coin, 'day')
            updateOnePoint(coin, 'week')
    print('This job is run every 5 minutes.')


def monthJob():
    for oneList in coins:
        for coin in oneList:
            updateOnePoint(coin, 'month')
    print('This job is run every 1 hour.')


def month3Job():
    for oneList in coins:
        for coin in oneList:
            updateOnePoint(coin, 'month3')
    print('This job is run every 2 hours.')


def yearJob():
    for oneList in coins:
        for coin in oneList:
            updateOnePoint(coin, 'year')
    print('This job is run every 1 day.')


def allJob():
    for oneList in coins:
        for coin in oneList:
            updateOnePoint(coin, 'all')
    print('This job is run every 2 days.')


def refreshCoinInfo():
    for oneList in coins:
        for coin in oneList:
            coinInfo = getCoinInfo(coin)
            saveCoinInfo(coinInfo)


def refreshExchangeInfo():
    infos = getExchangeInfos()
    for info in infos:
        saveExchangeInfo(info)


def refreshInfos():
    refreshCoinInfo()
    refreshExchangeInfo()


def refreshJob():
    for oneList in coins:
        for coin in oneList:
            refreshAllData(coin)

    refreshInfos()

    print('This job is run every weekday at 23pm.')



def start():

    refreshJob()
    # scheduler = BlockingScheduler()
    # scheduler.add_job(dayWeekJob, 'interval', minutes=5)
    # scheduler.add_job(monthJob, 'interval', hours=1)
    # scheduler.add_job(month3Job, 'interval', hours=2)
    # scheduler.add_job(yearJob, 'interval', days=1)
    # scheduler.add_job(allJob, 'interval', days=2)
    # scheduler.add_job(refreshInfo, 'interval', days=1)
    # scheduler.add_job(refreshJob, 'cron', day_of_week='sun', hour='0-3')
    #
    # try:
    #
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     pass

