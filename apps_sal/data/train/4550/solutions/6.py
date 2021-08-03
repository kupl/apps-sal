import datetime as dt
import datetime
import re
def seconds_ago(Q, S): return str(datetime.datetime(*map(int, re.split('[- :]', Q))) - datetime.timedelta(0, S))
