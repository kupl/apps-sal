def pattern(n):
    if n < 1:
        return ""
    pattern = "1"
    for i in range(2, n + 1):
        pattern += "\n" + (str(i) * i)
    return pattern
