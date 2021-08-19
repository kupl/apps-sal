LIMIT = 100000
values = set()
for i in range(4):
    values |= set(range(3 ** i, LIMIT, 5))


def number_increasing(n):
    return n in values
