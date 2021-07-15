def number(lines):
    n = 1
    n1 = []
    for i in lines:
        x = (str(n) + ": " + i)
        n1.append(x)
        n = n + 1
    return n1

