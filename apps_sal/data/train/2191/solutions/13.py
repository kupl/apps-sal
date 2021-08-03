N = 2000001
n = int(input())
a = list(set(map(int, input().split())))
prev = [0] * N
for x in a:
    prev[x] = x
for x in range(N):
    prev[x] = max(prev[x], prev[x - 1])
ans = 0
for x in a:
    for j in range(2 * x, N, x):
        ans = max(ans, prev[j - 1] % x)
print(ans)
