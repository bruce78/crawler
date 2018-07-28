import logging


logging.basicConfig(filename='../myapp.log', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main():
    # del_all()
    # print json.dumps(dump_all(), indent=4)
    print('Crawler start to schedule work!')

    from crawler.trend.jobs import start

    start()


if __name__ == '__main__':
    main()
