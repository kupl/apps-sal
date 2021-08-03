from operator import itemgetter
from heapq import heappush, heappop
N, M = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(N)]
LR.sort(key=itemgetter(1))
A = []
ans_left = 0
idx = 1
for _, r in LR:
    if r == M + 1 or idx == M + 1:
        break
    ans_left += 1
    idx = max(idx + 1, r + 1)

idx_LR = 0
q = []
for i in range(M + 1 - ans_left, M + 1):
    while idx_LR < N and LR[idx_LR][1] <= i:
        l, _ = LR[idx_LR]
        heappush(q, l)
        idx_LR += 1
    heappop(q)
while idx_LR < N:
    l, _ = LR[idx_LR]
    q.append(l)
    idx_LR += 1

q.sort(reverse=True)
ans_right = 0
idx = M
for l in q:
    if l == 0 or idx == 0 or ans_right + ans_left == M:
        break
    ans_right += 1
    idx = min(l - 1, idx - 1)
ans = N - ans_left - ans_right
print(ans)
