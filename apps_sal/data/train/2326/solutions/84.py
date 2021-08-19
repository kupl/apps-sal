N = int(input())
A = list(map(int, input().split()))
d = dict()
for (i, a) in enumerate(A):
    (j, cnt) = d.get(a, (N, 0))
    d[a] = (min(i, j), cnt + 1)
P = []
for (k, v) in d.items():
    P.append((k, v[0], v[1]))
P.sort(key=lambda x: x[0], reverse=True)
res = [0] * N
cnt = 0
k = N - 1
for i in range(len(P) - 1):
    (A0, i0, cnt0) = P[i]
    (A1, i1, cnt1) = P[i + 1]
    k = min(k, i0)
    cnt += cnt0
    res[k] += (A0 - A1) * cnt
(A1, i1, cnt1) = P[-1]
res[min(i1, k)] += A1 * (cnt + cnt1)
print(*res, sep='\n')
