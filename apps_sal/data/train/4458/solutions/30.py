import re
from datetime import time


def time_correct(t):
    print(t)
    if not t:
        return t
    if not re.match(r"\d\d:\d\d:\d\d", t):
        return None
    H, M, S = [int(item) for item in t.split(":")]

    m, s = (M + S // 60), S % 60
    h, m = (H + m // 60) % 24, m % 60

    return str(time(h, m, s))
