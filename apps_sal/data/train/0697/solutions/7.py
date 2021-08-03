for _ in range(int(input())):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    maxs = sum(a[:q])
    temp = maxs
    for i in range(q, n):
        temp = temp + a[i] - a[i - q]
        maxs = max(maxs, temp)
    print(maxs)
