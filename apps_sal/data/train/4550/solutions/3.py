from datetime import timedelta, datetime


def seconds_ago(s, n):
    #   return (datetime.fromisoformat(s) - timedelta(seconds = n)).isoformat(sep=' ')   # python ver >= 3.7
    return (datetime.strptime(s, "%Y-%m-%d %H:%M:%S") - timedelta(seconds=n)).strftime("%4Y-%m-%d %H:%M:%S")
