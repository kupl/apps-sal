t = int(input())
for _ in range(t):
    (k, n) = map(int, input().split())
    l = list(map(int, input().split()))
    f = -1
    s = -1
    for i in range(n):
        if l[i] == k:
            f = i
            break
    for i in range(n - 1, -1, -1):
        if l[i] == k:
            s = i
            break
    if f == -1 or s == -1:
        print(0)
    else:
        s += 1
        f += 1
        print(s - f)
