import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
e = set((tuple(map(int, input().split())) for _ in range(m)))
unknown = set(range(1, n + 1))
to_check = []
ans = 0
while unknown:
    if to_check:
        u = to_check.pop()
    else:
        u = unknown.pop()
        ans += 1
    cur = []
    for v in unknown:
        if (u, v) in e or (v, u) in e:
            continue
        cur.append(v)
    for v in cur:
        unknown.remove(v)
    to_check += cur
print(ans - 1)
