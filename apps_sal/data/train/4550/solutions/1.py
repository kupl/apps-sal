from datetime import datetime,timedelta

def seconds_ago(s,n):
    t = datetime.strptime(s,'%Y-%m-%d %H:%M:%S')-timedelta(seconds=n)
    return str(t.year).zfill(4)+t.strftime('-%m-%d %H:%M:%S')
