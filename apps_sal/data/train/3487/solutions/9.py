def level():
    n = 2
    while n:
        yield n ** 2
        n += 1

def beeramid(bonus, price):
    b, x, sum, n = bonus // price, level(), 1, 0
    while sum <= b:
        sum += next(x)
        n += 1
    return n
