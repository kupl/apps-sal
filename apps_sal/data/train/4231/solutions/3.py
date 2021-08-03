def a(n):
    n = n if n % 2 == 0 else n - 1
    width = 2 * n - 1
    lines = ["A".center(width)] + [("A" + " " * k + "A").center(width) for k in range(1, n - 1, 2)] +\
        [" ".join(["A"] * (n // 2 + 1)).center(width)] + [("A" + " " * k + "A").center(width) for k in range(n + 1, 2 * n - 1, 2)]
    return "\n".join(lines) if n >= 4 else ""
