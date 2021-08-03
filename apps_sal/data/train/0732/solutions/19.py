for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = d = r = 0
    for i in range(n):
        if c == d and a[i] == b[i]:
            r += a[i]
        c += a[i]
        d += b[i]
    print(r)
