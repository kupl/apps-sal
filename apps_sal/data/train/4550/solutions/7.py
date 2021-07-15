import datetime

seconds_ago = lambda s,n: str(datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(seconds=n))
