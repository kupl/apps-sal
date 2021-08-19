for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = set(l)
    for i in range(1, n):
        if l[i] == l[i - 1]:
            l[i] = -1
    m = 0
    sx = list(s)
    sx.sort()
    for i in sx:
        x = l.count(i)
        if m < x:
            m = x
            z = i
    print(z)
