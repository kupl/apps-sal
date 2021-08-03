n, a, b = map(int, input().split())
x = list(map(int, input().split()))
l = []
for i in range(n - 1):
    l.append(x[i + 1] - x[i])
ans = 0
for i in l:
    if a * i < b:
        ans += a * i
    else:
        ans += b
print(ans)
