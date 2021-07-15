def count_cows(n):
    if type(n) != int: return None
    a, b, c, d = 1, 0, 0, 0
    for _ in range(n):
        a, b, c, d = c + d, a, b, c + d       
    return a + b + c + d
