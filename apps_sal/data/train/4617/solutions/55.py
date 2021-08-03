def powers_of_two(n):
    result = []
    i = 0
    while i < n + 1:
        num = 2 ** i
        i += 1
        result.append(num)
    return result
