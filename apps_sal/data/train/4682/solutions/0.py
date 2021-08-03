import re
from datetime import date, timedelta


def date_correct(text):
    if not text:
        return text
    try:
        d, m, y = map(int, re.match(r'^(\d{2})\.(\d{2})\.(\d{4})$', text).groups())
        mo, m = divmod(m - 1, 12)
        return (date(y + mo, m + 1, 1) + timedelta(days=d - 1)).strftime('%d.%m.%Y')
    except AttributeError:
        return None
