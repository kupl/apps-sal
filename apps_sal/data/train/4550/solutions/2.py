from dateutil import parser
import datetime

def seconds_ago(s,n):
    timej = parser.parse(s) - datetime.timedelta(seconds=n)
    return  str(timej)
