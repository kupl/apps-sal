t = eval(input())
for qq in range(t):
    n = eval(input())
    s = input()
    amin = 0
    bmin = 0
    for x in s:
        if x == 'a':
            amin += 1
        else:
            bmin += 1
    for cc in range(n - 1):
        s = input()
        ca = 0
        cb = 0
        for x in s:
            if x == 'a':
                ca += 1
            else:
                cb += 1
        amin = min(ca, amin)
        bmin = min(cb, bmin)
    print(min(amin, bmin))
