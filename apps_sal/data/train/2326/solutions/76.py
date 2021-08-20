N = int(input())
a = list(map(int, input().split()))
D = []
for i in range(N):
    D.append((a[i], i))
D.append((0, -1))
D.sort(reverse=True)
ans = [0] * N
mi = float('inf')
for i in range(N):
    mi = min(mi, D[i][1])
    ans[mi] += (D[i][0] - D[i + 1][0]) * (i + 1)
for i in ans:
    print(i)
