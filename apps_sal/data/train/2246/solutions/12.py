import heapq as hp
R = lambda: map(int ,input().split())
n, k = R()
xs = list(R())
a, r, h = int(input()), 0, []
cs = list(R())
for i, x in enumerate(xs):
    hp.heappush(h, cs[i])
    while x > k and h:
        s = hp.heappop(h)
        k += a
        r += s
    if x > k:
        r = -1
        break
print(r)
