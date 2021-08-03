from datetime import datetime as dt
from itertools import permutations


def late_clock(a):
    li = []
    for i in permutations(list(map(str, a))):
        try:
            d = dt.strptime(f'{"".join(i[:2])}:{"".join(i[2:])}', "%H:%M")
        except:
            continue
        li.append(d)
    return str(min(li, key=lambda x: dt.now() - x))[11:16]
