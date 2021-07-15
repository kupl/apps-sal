def squares(x, n):
    result = [x] if n > 0 else []
    for i in range(0, n-1):
        result.append(result[-1]**2)
    return result
