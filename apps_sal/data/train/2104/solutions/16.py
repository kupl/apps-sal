n = int(input())
line = [int(x) for x in input().split()]
line.sort()
ans = (line[n - 1] - line[0]) * (line[-1] - line[n])
k = line[-1] - line[0]
for i in range(1, n):
    ans = min(ans, k * (line[i + n - 1] - line[i]))
print(ans)
