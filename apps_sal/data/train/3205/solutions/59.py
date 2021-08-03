def is_divisible(n, x, y):
    q1, r1 = divmod(n, x)
    q2, r2 = divmod(n, y)
    return True if r1 == 0 and r2 == 0 else False
