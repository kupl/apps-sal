def count_by(x, n):
    y = x
    result = [x]
    for i in range(n-1):
        y += x
        result.append(y)
    return result

