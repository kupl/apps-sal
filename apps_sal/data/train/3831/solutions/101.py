def angle(n):
    result = 180
    if n > 3:
        for i in range(n - 3): result += 180
    return result
