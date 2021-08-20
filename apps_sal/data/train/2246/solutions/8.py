import heapq as hp
(N, K) = map(int, input().split())
X = list(map(int, input().split()))
A = int(input())
C = list(map(int, input().split()))
limit = K
q = []
cost = 0
for (i, x) in enumerate(X):
    hp.heappush(q, C[i])
    if x > limit:
        while limit < x and q:
            limit += A
            nc = hp.heappop(q)
            cost += nc
        if limit < x:
            cost = -1
            break
print(cost)
