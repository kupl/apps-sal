from collections import defaultdict

a = list(map(ord, input()))
N = len(a)
La = ord("a")

data = [0] * (N + 1)


d = [[] for i in range(26)]
for i, c in enumerate(a):
    d[c - La].append(i)

odd = 0
for v in d:
    if len(v) % 2:
        odd += 1
if not odd <= N % 2:
    print((-1))
    return

data = [0] * (N + 1)


def add(k, x):
    while k <= N:
        data[k] += x
        k += k & -k


def get(k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s


M = [None] * N
for v in d:
    vl = len(v)
    for i in range(vl):
        if not i <= vl - 1 - i:
            break
        p = v[i]
        q = v[-i - 1]
        M[p] = q
        M[q] = p
cnt = 0
B = [0] * N
for i in range(N - 1, -1, -1):
    if M[i] <= i:
        B[i] = B[M[i]] = cnt
        cnt += 1

cur = -1
ans = 0
for i in range(N - 1, -1, -1):

    if cur < B[i]:
        cur = B[i]
        if M[i] == i:
            ans += N // 2 - cur
        else:
            ans += M[i] - get(M[i] + 1)
        add(M[i] + 1, 1)
print(ans)
