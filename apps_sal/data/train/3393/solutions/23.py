def list_squared(m, n):
    return [[i, square_sum(i)] for i in range(m, n + 1) if (square_sum(i)**0.5).is_integer()]


def square_sum(n):
    if n == 1:
        return 1
    div = []
    for i in range(1, int(n**0.5) + 1):
        if i in div:
            break
        if n % i == 0:
            div += [i, n // i] if i != n // i else [i]
    return sum(v**2 for v in div)
