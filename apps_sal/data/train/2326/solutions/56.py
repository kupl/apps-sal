N = int(input())
A = list(map(int, input().split()))
D = []
for (id, a) in enumerate(A):
    D.append([a, id])
D = sorted(D)[::-1]
D.append([0, 0])
cnt = [0] * N
minid = D[0][1]
for i in range(N):
    d = D[i][0] - D[i + 1][0]
    cnt[minid] += d * (i + 1)
    if D[i + 1][1] < minid:
        minid = D[i + 1][1]
for i in range(N):
    print(cnt[i])
