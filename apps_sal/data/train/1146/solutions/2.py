(N, D) = list(map(int, input().split()))
s = []
for _ in range(N):
    s.append(int(input()))
s.sort()
ans = 0
i = 0
while i < len(s) - 1:
    if s[i + 1] - s[i] <= D:
        ans += 1
        i += 1
    i += 1
print(ans)
