import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
ln = max(max(a), max(b)).bit_length() + 1
for i in range(ln):
    y = (1 << (i + 1))
    u = [x % y for x in a]
    v = [x % y for x in b]
    y >>= 1
    u.sort(reverse=True)
    v.sort()
    t = 0
    k = 0
    kk = 0
    for x in u:
        while k < N and x + v[k] < y:
            k += 1
        t += N - k
        while kk < N and x + v[kk] < y * 2:
            kk += 1
        t -= N - kk
    k = 0
    kk = 0
    for x in u:
        while k < N and x + v[k] < y * 2 + y:
            k += 1
        t += N - k
        while kk < N and x + v[kk] < y * 4:
            kk += 1
        t -= N - kk
    res ^= t % 2 * y
print(res)
