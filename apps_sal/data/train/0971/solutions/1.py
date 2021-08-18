for _ in range(int(input())):
    n = int(input())
    d = {}
    l = list(map(int, input().split()))
    for i in l:
        d[i] = l.count(i)
    x = 0

    for j in d:
        if d[j] > x:
            x = d[j]
    print(n - x)
