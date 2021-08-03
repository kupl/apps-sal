def count_by(x, n):
    result = list()
    temp = x
    for i in range(n):
        result.append(x)
        x += temp
    return result
