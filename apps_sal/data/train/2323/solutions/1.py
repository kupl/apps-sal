import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
A = [0] + list(map(int, readline().split()))
for i in range(1, N):
    A[i] += A[i-1]

INF = 10**9+7
B = [list(map(int, readline().split())) for _ in range(N)] + [[INF]*M] + [[0]*M]
right = [[0]*M for _ in range(N)]

for m in range(M):
    L = list(range(N))
    L.sort(key = lambda x: B[x][m])
    RR = list(range(1, N+3))
    LL = list(range(-1, N+1))
    for vn in L:
        vn += 1
        right[vn-1][m] = RR[vn]-1
        RR[LL[vn]] = RR[vn]
        LL[RR[vn]] = LL[vn]

diff = [0]*(N+1)
for m in range(M):
    diff[0] += B[0][m]
    pre = B[0][m]
    for i in range(1, N):
        if B[i][m] > pre:
            diff[i] += B[i][m]-pre
            pre = B[i][m]

offset = 0
ans = 0
for l in range(N):
    offset += diff[l]
    for m in range(M):
        if B[l][m] < B[l-1][m]:
            oldr = right[l-1][m]
            diff[oldr] -= B[oldr][m] - B[l-1][m]
            offset += B[l][m] - B[l-1][m]
            cnt = l
            while cnt < N and right[cnt][m] <= oldr:
                rcm = right[cnt][m]
                diff[rcm] += B[rcm][m] - B[cnt][m]
                cnt = rcm
    ans = max(ans, offset)
    roff = offset
    for r in range(l+1, N):
        roff += diff[r]
        ans = max(ans, roff - (A[r]-A[l]))
        #print(l, r, roff - (A[r] - A[l]))

print(ans)
