def between(a, b):
    s = [a]
    while s[-1] < b:
        t = s[-1] + 1
        s.append(t)
    return s
