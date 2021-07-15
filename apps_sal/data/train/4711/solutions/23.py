from itertools import count, takewhile
pow5 = lambda x: 5**x

def zeros(n):
    okay = lambda x: x <= n
    val  = lambda x: n//x
    return sum(map(val, takewhile(okay, map(pow5, count(1)))))
