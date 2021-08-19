n = int(input())
if n // 2 & 1:
    print(-1)
else:
    ans = [0] * (n + 1)
    for i in range(1, n // 2 + 1, 2):
        ans[i] = i + 1
        ans[i + 1] = n - i + 1
        ans[n - i + 1] = n - i
        ans[n - i] = i
    if n % 2:
        ans[n // 2 + 1] = n // 2 + 1
    print(*ans[1:])
