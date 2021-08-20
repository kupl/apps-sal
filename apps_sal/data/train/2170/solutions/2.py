import heapq


def calc(l, n):
    smol = l // n
    tol = l % n
    return smol * smol * n + (2 * smol + 1) * tol


(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
curr = [1] * n
q = []
for i in range(n):
    v = a[i]
    heapq.heappush(q, (calc(v, 2) - calc(v, 1), i))
out2 = sum([x * x for x in a])
for i in range(k - n):
    (diff, nex) = heapq.heappop(q)
    curr[nex] += 1
    v = a[nex]
    heapq.heappush(q, (calc(v, curr[nex] + 1) - calc(v, curr[nex]), nex))
    out2 += diff
out = 0
for i in range(n):
    out += calc(a[i], curr[i])
assert out == out2
print(out)
