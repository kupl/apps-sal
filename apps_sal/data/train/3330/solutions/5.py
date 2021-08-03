def make_triangle(m, n):
    count = 0
    rec = n - m + 1
    for i in range(1, 99999999):
        count += i
        if count > rec:
            return ""
        elif count == rec:
            limit = i
            break
    right = limit
    left = 0
    triangle = [[" "] * i for i in range(1, limit + 1)]
    while m <= n:
        for i in range(left, right):
            triangle[i + left][i] = str(m % 10)
            m += 1
        right -= 1
        for i in range(right - 1, left - 1, -1):
            triangle[right + left][i] = str(m % 10)
            m += 1
        right -= 1
        for i in range(right, left, -1):
            triangle[i + left][left] = str(m % 10)
            m += 1
        left += 1
    res = []
    for j, i in enumerate(triangle):
        res.append(" " * (limit - (j) - 1) + " ".join(i))
    return "\n".join(res)
