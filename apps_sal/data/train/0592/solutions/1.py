def memo(func):
    cache = {}

    def f(*args):
        if args in cache:
            return cache[args]
        r = func(*args)
        cache[args] = r
        return r
    return f


def doit():
    s = input().strip()
    words = set([input().strip() for x in range(eval(input()))])

    @memo
    def g(start, end):
        num = set([])
        if start >= end:
            return 0
        for w in words:
            x = start
            while x + len(w) <= end:
                r = s.find(w, x, end)
                if r == -1:
                    break
                num.add(g(start, r) ^ g(r + len(w), end))
                x = r + 1
        x = 0
        while x in num:
            x += 1
        return x
    return g(0, len(s)) > 0


n = eval(input())
for x in range(n):
    if doit():
        print('Teddy')
    else:
        print('Tracy')
