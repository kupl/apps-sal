(m, n) = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
(ans, w, q) = (0, 0, m)
for m in range(q):
    if arr[m] > n:
        w = 1
        break
    ans += 1 + arr[m] * (arr[m] + 1) // 2
    n -= arr[m]
print(ans) if n == 0 else print(ans + q - m + n * (n + 1) // 2) if w == 1 else print(ans)
