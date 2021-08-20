def ordern(n):
    p = 1
    while n > 0:
        n = n // 10
        p = p * 10
    return p


def automorphic(n):
    square = n * n
    order = ordern(n)
    if square % order == n:
        return 'Automorphic'
    else:
        return 'Not!!'
