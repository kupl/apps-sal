from sys import stdin
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)][::-1]
(res, curr) = ([-1] * n, 0)
for q in queries:
    if q[0] == 1:
        if res[q[1] - 1] == -1:
            res[q[1] - 1] = max(q[2], curr)
    else:
        curr = max(curr, q[1])
for i in range(n):
    if res[i] == -1:
        res[i] = max(curr, arr[i])
res = [str(q) for q in res]
print(' '.join(res))
