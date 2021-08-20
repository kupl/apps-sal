from datetime import timedelta, datetime


def seconds_ago(s, n):
    return (datetime.strptime(s, '%Y-%m-%d %H:%M:%S') - timedelta(seconds=n)).strftime('%4Y-%m-%d %H:%M:%S')
