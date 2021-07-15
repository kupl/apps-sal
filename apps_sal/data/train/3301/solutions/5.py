from bisect import bisect_left

def gen():
    x, y = 0, 1
    while True:
        yield y
        x, y = y, x+y
fib, memo, res = gen(), [0], [0]

def even_fib(m):
    while m > memo[-1]:
        val = next(fib)
        if val % 2 == 0:
            memo.append(val)
            res.append(res[-1] + val)
    return m > 0 and res[bisect_left(memo, m)-1]
