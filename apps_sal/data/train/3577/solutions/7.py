def fast_fib(n):
    def pos(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = pos(n // 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if n % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)

    def fib(n):
        if n >= 0:
            return pos(n)[0]

        if n < 0:
            sign = -1 if n % 2 == 0 else 1
            return sign * pos(abs(n))[0]

    return fib(n)


def fib_digits(n):
    from collections import Counter
    cnt = Counter(str(fast_fib(n)))
    ret = [(v, int(k)) for k, v in cnt.items()]
    ret = sorted(ret, key=lambda x: (-x[0], -x[1]))

    return ret
