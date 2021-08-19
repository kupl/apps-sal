n = int(input())
a = list(map(int, input().split()))
l = [(0, n)]
for (i, A) in enumerate(a):
    l.append((A, i))
l.sort(reverse=True)
ans = [0] * n
mi = float('inf')
for i in range(n):
    if mi > l[i][1]:
        mi = l[i][1]
    ans[mi] += (i + 1) * (l[i][0] - l[i + 1][0])
for i in range(n):
    print(ans[i])
