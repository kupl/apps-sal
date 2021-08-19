t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = 0
    for i in range(n):
        m = max(m, a[i] * b[i])
    ans = -1
    r = 0
    for i in range(n):
        if m == a[i] * b[i]:
            if r < b[i]:
                ans = i
                r = b[i]
    print(ans + 1)
