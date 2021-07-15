import collections

def is_dd(n):
    counter = collections.Counter(str(n))
    return any(counter[str(i)] == i for i in range(1, 10))
