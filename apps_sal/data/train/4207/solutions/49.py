def sum_cubes(n):
    result = [0]
    if n == 1:
        return 1
    while n > 0:
        result.append(n ** 3)
        n -= 1
    return sum(result)
