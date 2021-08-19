from bisect import bisect_right
input()
t = list(map(int, input().split()))
(s, p) = (0, [])
for (i, j) in enumerate(t):
    k = bisect_right(p, j)
    s += i - k
    p.insert(k, j)
print(2 * s - (s & 1))
