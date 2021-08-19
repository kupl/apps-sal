import re
import datetime as dt


def time_correct(text):
    if not text:
        return text
    try:
        (h, m, s) = map(int, re.match('^(\\d{2}):(\\d{2}):(\\d{2})$', text).groups())
        (mo, m) = divmod(m - 1, 60)
        return (dt.datetime.combine(dt.date(1, 1, 1), dt.time((h + mo) % 24, m + 1, 1)) + dt.timedelta(seconds=s - 1)).strftime('%H:%M:%S')
    except AttributeError:
        return None
