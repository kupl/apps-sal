def solve(st):
    b = list(st)
    c = []
    for i in range(len(st)):
        c.append(ord(b[i]))
    for i in c:
        if c.count(i) != 1:
            return False
    for i in range(min(c), max(c)):
        if i + 1 not in c:
            return False
    return True
