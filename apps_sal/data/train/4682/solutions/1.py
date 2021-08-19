import datetime as dt
import re


def date_correct(date):
    if isinstance(date, str) and re.fullmatch('\\d\\d\\.\\d\\d\\.\\d{4}', date):
        (d, m, y) = map(int, date.split('.'))
        (nM, m) = divmod(m - 1, 12)
        y += nM
        m += 1
        d = dt.date(y, m, 1) + dt.timedelta(days=d - 1)
        return f'{d.day:02}.{d.month:02}.{d.year:02}'
    if date == '':
        return ''
