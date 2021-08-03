def pattern(n):
    x = 1
    new = ""
    while x < n + 1 and n > 0:
        new += str(x) * x + '\n'
        x += 1
    return new[0:len(new) - 1]
