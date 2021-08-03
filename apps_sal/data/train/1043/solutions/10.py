for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(map(str, input().split()))
    li = []
    t = 0
    for i in range(k):
        a = list(map(str, input().split()))
        l = len(a)
        for j in range(l):
            li.append(a[j])
    d = []
    for i in range(n):
        if s[i] in li:
            d.append('YES')
        else:
            d.append('NO')
    print(*d)
