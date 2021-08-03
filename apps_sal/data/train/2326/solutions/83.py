import bisect

N = int(input())
A = list(map(int, input().split()))

inc = [[A[0], 0]]
for i in range(1, N):
    if A[i] > inc[-1][0]:
        inc.append([A[i], i])

n = len(inc)
test = inc[:n - 1]
query = [[] for i in range(n)]
for i in range(0, N):
    r = bisect.bisect_left(test, [A[i], i])
    query[r].append(A[i])

ans = [0 for i in range(N)]
count = 0
for i in range(n - 1, 0, -1):
    fr = inc[i][0]
    to = inc[i - 1][0]
    val = count * (fr - to) + sum(query[i]) - to * len(query[i])
    ans[inc[i][1]] = val
    count += len(query[i])

fr = inc[0][0]
to = 0
val = count * (fr - to) + sum(query[0]) - to * len(query[0])
ans[0] = val

for i in range(N):
    print(ans[i])
