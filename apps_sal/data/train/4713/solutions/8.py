from itertools import *
from datetime import *


def late_clock(digits):
    dt = []
    for (a, b, c, d) in permutations(digits, 4):
        try:
            dt.append(datetime.strptime(f'{a}{b}:{c}{d}', '%H:%M'))
        except:
            pass
    return max(dt).strftime('%H:%M')
