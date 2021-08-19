import bisect
t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    arr = list(map(int, input().split()))
    seti = set(arr)
    f = 1
    for i in range(1, m):
        if i not in seti:
            f = 0
            break
    if f == 0:
        print(-1)
    elif m in seti:
        print(n - arr.count(m))
    else:
        print(n)
