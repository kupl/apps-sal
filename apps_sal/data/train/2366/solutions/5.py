t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mi = 10000000
    ans = 0
    i = n - 1
    while (i >= 0):
        if a[i] > mi:
            ans += 1
        if a[i] < mi:
            mi = a[i]
        i -= 1
    print(ans)
