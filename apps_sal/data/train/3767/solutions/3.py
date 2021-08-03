from string import ascii_uppercase as u
from math import factorial as f
d = list('0123456789') + list(u)
d_ = dict(map(lambda x: x[::-1], enumerate(d)))


def dec2FactString(n):
    reminders, i = '', 1
    while n:
        n, b = divmod(n, i)
        reminders += d[b]
        i += 1
    return reminders[::-1]


def factString2Dec(n): return sum([d_[n[-(i + 1)]] * f(i) for i in range(len(n) - 1, -1, -1)])
