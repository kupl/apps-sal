def solve(s, g):
    lst = []
    for i in range(1, s):
        if i % g == 0:
            lst.append(i)
    for i in lst:
        if i + g == s:
            a = [i] + [g]
            a = sorted(a)
            return (a[0], a[1])
    return -1
