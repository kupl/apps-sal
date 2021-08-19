import time
import re


def time_correct(t):
    if t == '':
        return ''
    elif t is None or not re.match('\\d{2}:\\d{2}:\\d{2}', t):
        return None
    else:
        (h, m, s) = [int(i) for i in t.split(':')]
        return f"{time.strftime('%H:%M:%S', time.gmtime(3600 * h + 60 * m + s))}"
