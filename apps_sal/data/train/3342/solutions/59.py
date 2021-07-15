def pattern(n):
    pattern = ""
    if n < 1:
        return pattern
    for i in range(1, n + 1):
        pattern += i * str(i)
        if i < n:
            pattern += "\n"
    return pattern
