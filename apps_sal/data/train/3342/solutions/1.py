def pattern(n):
    result = ''
    for i in range(1, n + 1):
        result += str(i) * i + '\n'
    return result[:-1]
