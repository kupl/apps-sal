def mark_spot(n):
    if type(n) is not int or n <= 0 or n % 2 == 0:
        return "?"

    p1, s = 0, 2 * n - 3
    result = ""
    for i in range(1, n // 2 + 1):
        result += " " * p1 + "X" + " " * s + "X\n"
        p1 += 2
        s -= 4
    result += " " * p1 + "X\n"
    for i in range(n // 2 + 2, n + 1):
        p1 -= 2
        s += 4
        result += " " * p1 + "X" + " " * s + "X\n"

    return result
