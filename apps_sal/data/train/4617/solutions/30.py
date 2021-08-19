def powers_of_two(n):
    result = [1]
    for i in range(1, n + 1):
        result.append(2 ** i)
    return result
