def count_by(x, n):
    return list(range(0, (n + 1) * x, x)[1:])


print(count_by(2, 5))
