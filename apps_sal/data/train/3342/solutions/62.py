def pattern(n):
    if n < 1:
        return ""
    if n == 1:
        return "1"
    else:
        return pattern(n - 1) + "\n" + str(n) * n
