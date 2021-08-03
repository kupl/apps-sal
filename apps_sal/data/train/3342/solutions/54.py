def pattern(n):
    s = ""
    for i in range(1, n + 1):
        s += str(i) * i
        if i == n:
            break
        s += "\n"
    return s
