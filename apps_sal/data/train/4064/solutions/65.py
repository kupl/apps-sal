def count_by(x, n):
    start = x
    result = list()
    while start <= x * n:
        result.append(start)
        start += x
    return result
