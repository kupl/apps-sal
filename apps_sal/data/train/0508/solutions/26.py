from bisect import bisect_left

n, q = map(int, input().split())
stx = [list(map(int, input().split())) for _ in range(n)]
d = [int(input()) for _ in range(q)]

INF = 10 ** 9 + 1

stx.sort(key=lambda x: x[2])

nxt = [-1] * q
ans = [-1] * q

for s, t, x in stx:
    l = bisect_left(d, s - x)
    r = bisect_left(d, t - x)

    while l < r:
        if nxt[l] == -1:
            ans[l] = x
            nxt[l] = r
            l += 1
        else:
            l = nxt[l]

print(*ans, sep="\n")
