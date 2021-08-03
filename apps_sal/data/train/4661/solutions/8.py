def pattern(n):
    return "\n".join(" " * (n - 1 - i) + "".join([str(i % 10) for i in range(1, n + 1)]) + " " * i for i in range(n))
