3
n = int(input())
l = []
for i in range(n):
    (a, b, c, d) = list(map(int, input().split()))
    l.append((a, b, c, d))
ans = 1
for i in range(1, n):
    if sum(l[i]) > sum(l[0]):
        ans += 1
print(ans)
