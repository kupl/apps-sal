n = int(input())
a = list(map(int, input().split()))
b = [[a[i], i] for i in range(n)]
b.sort(reverse=True)
d = {}
dcnt = {}
for i in range(n):
    if not a[i] in d:
        d[a[i]] = i
        dcnt[a[i]] = 1
    else:
        dcnt[a[i]] = dcnt[a[i]] + 1
b = [[0, 0] for _ in range(len(d) + 1)]
k = 0
for i, j in d.items():
    b[k][0], b[k][1] = i, j
    k += 1
b.sort(reverse=True)
ans = [0] * n
j = b[0][1]
cnt = 0
for i in range(len(d)):
    cnt += dcnt[b[i][0]]
    j = min(j, b[i][1])
    ans[j] += (b[i][0] - b[i + 1][0]) * cnt
for i in ans:
    print(i)
