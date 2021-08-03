t = eval(input())
while t != 0:
    cnt = 0
    t -= 1
    n = eval(input())
    a = list(map(int, input().split()))
    s = []
    for i in range(1, n + 1):
        pos = a[i - 1]
        if pos == 0:
            s.insert(0, i)
        else:
            pos = s.index(a[i - 1])
            cnt += min(pos + 1, i - 2 - pos)
            s.insert(pos + 1, i)
    print(cnt)
