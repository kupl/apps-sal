t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    m = max(s)
    c = []
    for i in range(n):
        if s[i] == m:
            c.append(i)
    if len(c) == 1:
        print(n // 2)
    elif c[-1] - c[0] + 1 > n // 2:
        print(0)
    else:
        x = c[-1] - c[0]
        print(n // 2 - x)
