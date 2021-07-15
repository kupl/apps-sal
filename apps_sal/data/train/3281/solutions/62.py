from datetime import datetime
from functools import reduce

def unlucky_days(year):
    return reduce(lambda r, month: r + int(datetime.strptime(f'{year}-{month:02}-13', '%Y-%m-%d').weekday() == 4), range(1,13), 0)
