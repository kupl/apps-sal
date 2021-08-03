import datetime


def seconds_ago(s, n):
    d = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(seconds=-n)
    return d.strftime('%Y').rjust(4, '0') + d.strftime('-%m-%d %H:%M:%S')
