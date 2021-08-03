from collections import Counter
n = int(input())
A = tuple(map(int, input().split()))
C = Counter(A)
ans = [0 for _ in range(n)]
D = dict()
S = set(A)
if len(S) == 1:
    print((sum(A)))
    for _ in range(n - 1):
        print((0))
    return()
X = sorted(S, reverse=True)
for i, x in enumerate(X):
    D[x] = i

index = [n + 1 for _ in range(len(S))]
for i, a in enumerate(A):
    index[D[a]] = min(index[D[a]], i)

cnt = 0
x = n + 1

for i in range(1, len(S)):
    tmp = X[i - 1]
    nxt = X[i]
    cnt += C[tmp]
    x = min(x, index[D[tmp]])
    ans[x] += (tmp - nxt) * cnt

for i, a in enumerate(A):
    if a != 0:
        cnt += C[nxt]
        ans[i] += nxt * cnt
        break

for a in ans:
    print(a)
