n, ans = int(input()), 0
a = [0, 0] + list(map(int, input().split()))
s = [0] + [i if i != -1 else 1e9 + 1 for i in map(int, input().split())]
for i in range(1, n + 1):
    s[a[i]] = min(s[a[i]], s[i])
for i in range(1, n + 1):
    if s[a[i]] > s[i]:
        print(-1)
        return
    if s[i] == 1e9 + 1:
        s[i] = s[a[i]]
    ans += s[i] - s[a[i]]
print(ans)
