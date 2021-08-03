for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    p = q = c = 0
    r = s = 1001
    for i in range(x):
        a = input()
        for j in range(y):
            if a[j] == '*':
                c = 1
                # print i,j
                if i > p:
                    p = i
                if j > q:
                    q = j
                if i < r:
                    r = i
                if j < s:
                    s = j
    g = p - ((p + r) // 2)
    h = q - ((q + s) // 2)
    if c:
        c += max(g, h)
    print(c)
