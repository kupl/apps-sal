def odd(s):
    odd = 0
    l = [x for x in s]
    while True:
        try:
            o = l.index('o')
            d1 = l.index('d', o)
            d2 = l.index('d', d1 + 1)
        except ValueError:
            return odd
        if o > -1 and d1 > -1 and d2 > -1:
            l.pop(d2)
            l.pop(d1)
            l.pop(o)
            odd += 1
        else:
            return odd
