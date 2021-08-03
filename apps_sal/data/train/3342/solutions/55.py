def pattern(n):
    return "" if n < 1 else "\n".join([str(i) * i for i in range(n + 1)])[1:]
