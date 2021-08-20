from sys import stdin
(n, m) = list(map(int, stdin.readline().strip().split()))
s = list(map(int, stdin.readline().strip().split()))
mx = 200000
arr = [-1 for i in range(mx + 1)]
visited = [False for i in range(mx + 1)]
cnt = [0 for i in range(mx + 1)]
for i in range(n):
    arr[s[i]] = i
x = 0
ans = 0
inf = mx + 30
while x < n:
    ind = arr[s[x]]
    v = []
    l = x
    while x <= ind and x < n:
        ind = max(arr[s[x]], ind)
        v.append(s[x])
        cnt[s[x]] += 1
        x += 1
    aux = 0
    for i in v:
        aux = max(aux, cnt[i])
    ans += x - l - aux
print(ans)
