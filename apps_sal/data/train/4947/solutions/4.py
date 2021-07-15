from itertools import izip as zip, islice

def sel_number(n, d):
    def ok(x):
        s = map(int, str(x))
        return all(0 < b-a <= d for a, b in zip(s, islice(s, 1, None)))
    return sum(ok(i) for i in range(12, n+1))
