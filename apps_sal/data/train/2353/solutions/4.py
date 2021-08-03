n = int(input())
data = list(map(int, input().split()))

sorted_data = sorted(data)

ans = {}
for i in range(0, n):
    ans[sorted_data[i]] = sorted_data[(i + 1) % n]

for v in data:
    print(ans[v], end=' ')
