def digitize(n):
    result = []
    if n == 0:
        return [0]
    while n:
        result.append(n % 10)
        n //= 10
    return result
