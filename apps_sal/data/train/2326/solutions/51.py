from heapq import heapify, heappop
N = int(input())
A = list(map(int, input().split()))
que = [(-a, i + 1) for (i, a) in enumerate(A)]
heapify(que)
ans = [0] * (N + 1)
cnt = 0
while que:
    (a, now) = heappop(que)
    cnt += 1
    ans[now] = -a * cnt
    while que and que[0][1] > now:
        (a, _) = heappop(que)
        ans[now] += -a
        cnt += 1
    if que:
        ans[now] -= -que[0][0] * cnt
print(*ans[1:], sep='\n')
