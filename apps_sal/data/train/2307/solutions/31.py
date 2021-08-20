(n, a, b) = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    d = x[i] - x[i - 1]
    if d * a < b:
        ans += d * a
    else:
        ans += b
print(ans)
