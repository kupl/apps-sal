def inpl(): return map(int, input().split())


N, T = inpl()
A = tuple(inpl())
m = A[0]
benefit = 0
pairs = 0
ans = 0

for i in range(1, N):
    a = A[i]
    d = a - m
    if d < 0:
        m = a
    elif d < benefit:
        continue
    elif d == benefit:
        pairs += 1
    elif d > benefit:
        ans = max(ans, pairs)
        benefit = d
        pairs = 1

ans = max(ans, pairs)
print(ans)
