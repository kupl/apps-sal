(n, s) = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
ans = 0
for i in range(len(a) // 2):
    if a[i] > s:
        ans += a[i] - s
ans += abs(a[len(a) // 2] - s)
for i in range(len(a) // 2 + 1, len(a)):
    if s > a[i]:
        ans += s - a[i]
print(ans)
