def pascal(p):
    t = [[1]]
    for _ in range(2, p + 1):
        t.append([1] + [a + b for (a, b) in zip(t[-1][:-1], t[-1][1:])] + [1])
    return t
