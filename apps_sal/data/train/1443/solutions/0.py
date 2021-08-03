for i in range(int(input())):
    n, k = map(int, input().split())
    m = []
    for j in range(n):
        l = list(input())
        m.append(l)
    a = 0
    for k in range(k):
        b = 0
        for p in range(n):
            if m[p][k] == '1':
                b += 1
        if b > 1:
            a += ((b * (b - 1)) // 2)
    print(a)
