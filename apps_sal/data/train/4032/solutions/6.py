from itertools import accumulate
def solve(n):
    a = [1]
    for _ in range(n):
        a = list(accumulate(a))
        a += a[-1:]
    return a[-1]
