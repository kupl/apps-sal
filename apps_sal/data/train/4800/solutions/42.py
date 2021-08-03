from itertools import count


def hotpo(n):
    for i in count():
        if n == 1:
            return i
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
