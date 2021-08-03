def digitize(n):
    result = []
    while n > 0:
        result.append(n % 10)
        n = int(n / 10)
    return result
