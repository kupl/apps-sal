def rectangles(n, m):
    result = 0

    if n < 2 or m < 2:
        return result

    for i in range(n):
        for j in range(m):
            result += i * j

    return result
