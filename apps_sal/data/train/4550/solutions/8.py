from datetime import datetime, timedelta


def seconds_ago(s, n):
    time = datetime.strptime(s, '%Y-%m-%d %H:%M:%S') - timedelta(seconds=n)
    return str(time)
