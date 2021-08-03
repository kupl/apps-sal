from itertools import count, takewhile
def pow5(x): return 5**x


def zeros(n):
    def okay(x): return x <= n
    def val(x): return n // x
    return sum(map(val, takewhile(okay, map(pow5, count(1)))))
