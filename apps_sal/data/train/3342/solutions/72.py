def pattern(n):
    return "\n".join("".join(str(i) for _ in range(i)) for i in range(1, n + 1))
