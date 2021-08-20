def f(x):
    return x[1]


for t in range(int(input())):
    n = int(input())
    s = ''
    l = []
    for i in range(n):
        (a, p) = list(map(int, input().split()))
        l.append((a, p))
    l = sorted(l, key=f, reverse=True)
    for i in range(n):
        (a, p) = l[i]
        a = a * p
        p -= 1
        if a == 0:
            continue
        if p == 0:
            s += ' + ' + str(a)
        else:
            s += ' + ' + str(a) + 'x^' + str(p)
    s = s[3:]
    if len(s) == 0:
        print(0)
    else:
        print(s)
