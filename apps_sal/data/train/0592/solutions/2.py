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
        x = start
        while x <= end:
            y = x
            while y <= end:
                if s[x:y + 1] in words:
                    num.add(g(start, x - 1) ^ g(y + 1, end))
                y += 1
            x += 1
        x = 0
        while x in num:
            x += 1
        return x
    return g(0, len(s) - 1) > 0


n = eval(input())
for x in range(n):
    if doit():
        print('Teddy')
    else:
        print('Tracy')
