def divisible_by(n, d):
    result = []
    for x in n:
        if x % d == 0:
            result.append(x)
    return result
