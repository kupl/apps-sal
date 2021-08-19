q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    u = [0] * n
    for i in range(n):
        u[a[i] - 1] += 1
    u.sort(reverse=1)
    k = u[0]
    ans = k
    for i in range(1, n):
        if u[i] >= u[i - 1]:
            u[i] = u[i - 1] - 1
            if u[i] <= 0:
                break
        ans += u[i]
    print(ans)
    # print(u)
