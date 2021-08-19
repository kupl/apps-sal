for _ in range(int(input())):
    (m, n) = map(int, input().split())
    x = []
    s = str(n)
    a = '9'
    for i in range(len(s)):
        if int(a) <= n:
            x.append(a)
            a += '9'
        else:
            break
    p = m * len(x)
    if p == 0:
        print('0 0')
    else:
        print(p, m)
