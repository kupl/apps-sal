from sys import stdin
for _ in range(int(stdin.readline())):
    (N, D) = list(map(int, stdin.readline().split()))
    _list = list(map(int, stdin.readline().split()))
    _list.sort()
    l = 0
    r = 2000000000.0
    precision = 1e-05
    for i in range(70):
        m = (l + r) / 2
        possible = True
        curr = 0
        for j in _list:
            if j > curr:
                curr = j
            if curr + precision > j + D:
                possible = 0
                break
            curr += m
        if possible:
            l = m
        else:
            r = m
    print(round(l, 10))
