import datetime
import re
def date_correct(date):
    if not date:
        return date
    if not re.fullmatch(r'(\d\d\.){2}\d{4}',date):
        return None
    d,m,y = [int(x) for x in date.split('.')]
    if m>12:
        y += m // 12
        m %= 12
        if not m:
            m = 12
            y -= 1
    return (datetime.datetime(year=y,month=m,day=1)+datetime.timedelta(days=d-1)).strftime("%d.%m.%Y")

