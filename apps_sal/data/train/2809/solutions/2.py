def digitize(n):
    result = []
    while n >= 1:
        result.append(n%10)
        n //= 10
    return result
