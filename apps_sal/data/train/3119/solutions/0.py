def pattern(n, *y):
    if n < 1:
        return ""
    y = y[0] if y and y[0] > 0 else 1
    result = []
    for j in range(1, n + 1):
        line = " " * (j - 1) + str(j % 10) + " " * (n - j)
        result.append(line + line[::-1][1:])
    return "\n".join(((result + result[::-1][1:-1]) * y)) + "\n" + result[0]
