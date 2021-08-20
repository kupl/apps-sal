def zeros(n):
    result = 0
    i = 5
    while n / i >= 1:
        result += int(n / i)
        i *= 5
    return int(result)
