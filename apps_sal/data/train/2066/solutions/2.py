n = int(input())
v = sorted([int(i) for i in input().split()])
ans = 2 ** 40
for i in range(n//2):
    ans = min(ans, v[i + n//2] - v[i])
print(ans)


