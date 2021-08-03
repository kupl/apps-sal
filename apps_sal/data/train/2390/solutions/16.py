q = int(input())
for j in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in a:
        b[i - 1] += 1
    b.sort()
    k = b[n - 1] + 1
    ans = 0
    for i in range(n - 1, -1, -1):
        if b[i] >= k:
            b[i] = k - 1
        k = b[i]
        ans += max(0, b[i])
    print(ans)
