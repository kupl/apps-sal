def square_gen(n):
    x = 1
    while x <= n:
        yield x
        x *= 2


def halving_sum(n):
    return sum([int(n / i) for i in square_gen(n)])
