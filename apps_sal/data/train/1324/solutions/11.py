t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    ans = -1
    l = []
    for i in range(int(n ** 0.5) + 1, 0, -1):
        if n % i == 0:
            l += [i]
            l += [n // i]
    l.sort(reverse=True)
    for i in l:
        if n // i >= k * (k + 1) // 2:
            ans = i
            break
    print(ans)
