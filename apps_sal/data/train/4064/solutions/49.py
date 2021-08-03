def count_by(x, n):
    result = []
    y = 1
    for number in range(n):
        result.append(x * y)
        y += 1
    return result
