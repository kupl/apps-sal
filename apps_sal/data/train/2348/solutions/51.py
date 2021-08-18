import bisect
n = int(input())
x = list(map(int, input().split()))
l = int(input())
q = int(input())
ab = [list(map(int, input().split())) for i in range(q)]

keta = len(format(n + 1, "b"))
nxt = [[0 for _ in range(n)] for _ in range(keta)]

for i in range(n):
    num = x[i] + l
    ind = bisect.bisect_right(x, num)
    nxt[0][i] = ind - 1

for k in range(1, keta):
    for i in range(n):
        nxt[k][i] = nxt[k - 1][nxt[k - 1][i]]


def solve(s, g, day):
    bi = format(day, "b")
    keta = len(bi) - 1

    for b in bi:
        if b == "1":
            s = nxt[keta][s]
        keta -= 1

    return s >= g


for a, b in ab:
    s = min(a, b)
    g = max(a, b)
    l = 0
    r = n
    while r - l > 1:
        mid = (l + r) // 2
        if solve(s - 1, g - 1, mid):
            r = mid
        else:
            l = mid

    print(r)
