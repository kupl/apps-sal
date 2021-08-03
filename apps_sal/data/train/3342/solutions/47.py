def pattern(n):
    return "\n".join(["".join([str(num)] * num) for num in range(1, n + 1)])
