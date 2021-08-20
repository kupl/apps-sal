(n, d) = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
i = 1
ans = 0
while i <= len(l) - 1:
    if l[i] - l[i - 1] <= d:
        ans += 1
        i += 2
    else:
        i += 1
print(ans)
