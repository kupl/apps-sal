def pattern(n, x=1, y=1, *args):
    if n < 1:
        return ""
    result = []
    for i in range(1, n + 1):
        line = " " * (i - 1) + str(i % 10) + " " * (n - i)
        result.append((line + line[::-1][1:]) + (line[1:] + line[::-1][1:]) * (x - 1))
    return "\n".join((result + result[::-1][1:]) + (result[1:] + result[::-1][1:]) * (y - 1))

