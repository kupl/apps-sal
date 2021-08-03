from re import match
from datetime import date as ymd, timedelta
def date_correct(date): return "" if date == "" else None if date == None or not match("\d\d\.\d\d\.\d{4}", date or "") else (lambda d, m, y: (ymd(y + (m - 1) // 12, (m - 1) % 12 + 1, 1) + timedelta(d - 1)).strftime("%d.%m.%Y"))(*map(int, date.split(".")))
