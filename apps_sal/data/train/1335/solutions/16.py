n = int(input())
l = list(map(int, input().split()))
d = {}
days = {}
ans = 0
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for (key, value) in d.items():
    if d[key] % 2 == 0:
        ans += d[key] // 2
    else:
        ans = ans + d[key] // 2 + 1
print(ans)
