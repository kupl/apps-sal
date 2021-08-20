import datetime


def seconds_ago(s, n):
    return str(datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S') - datetime.timedelta(seconds=n))
