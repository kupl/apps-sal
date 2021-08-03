from datetime import date, timedelta
import re


def date_correct(s):
    if s == '':
        return ''
    try:
        m = re.match(r'\A(\d{2})\.(\d{2})\.(\d{4})\Z', s)
    except:
        return None
    if not m:
        return None
    d, m, y = map(int, m.groups())
    d -= 1
    cy, m = divmod(m - 1, 12)
    return (date(y + cy, m + 1, 1) + timedelta(d)).strftime('%d.%m.%Y')
