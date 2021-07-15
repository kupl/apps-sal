def zeros(n):
    sum = 0
    d = 5
    while d <= n:
        sum += n // d
        d *= 5
    return sum
