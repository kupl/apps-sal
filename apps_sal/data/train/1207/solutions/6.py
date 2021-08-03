t = int(input())
for kk in range(t):
    n = int(eval(input()))
    a = [int(x) for x in input().split()]
    k = min(a)
    s = 0
    for i in range(n):
        if a[i] != k:
            s += k * a[i]
    print(s)
