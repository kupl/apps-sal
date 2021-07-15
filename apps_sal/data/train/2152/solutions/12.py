def simple_div(x):
    if not x & 1:
        yield 2
        while not x & 1:
            x >>= 1
    i = 3
    while i * i <= x:
        if x % i == 0:
            yield i
            while x % i == 0:
                x //= i
        i += 2
    if x != 1:
        yield x

def __main__():
    n = int(input())
    a = list(map(int, input().split()))
    sa = sum(a)
    a.pop()
    if sa == 1:
        print(-1)
        return
    res = 2**64
    for d in simple_div(sa):
        tmp = 0
        m = 0
        for x in a:
            m = (x + m) % d
            tmp += m if m * 2 <= d else d - m
        if tmp < res:
            res = tmp
    print(res)

__main__()

