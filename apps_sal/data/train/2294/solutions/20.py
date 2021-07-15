import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
X = []
mih, mah, mil, mal = 10 ** 9, 0, 10 ** 9, 0
for _ in range(N):
    x, y = map(int, input().split())
    x, y = min(x, y), max(x, y)
    X.append((x, y))
    mih = min(mih, y)
    mah = max(mah, y)
    mil = min(mil, x)
    mal = max(mal, x)

ans = (mal - mil) * (mah - mih)

Y = []
for x, y in X:
    if mih <= x <= mal or mih <= y <= mal:
        continue
    Y.append((x, y))

Y = sorted(Y, key = lambda a: a[0])
Z = [(0, mal)]
may = 0
for x, y in Y:
    if y > may:
        Z.append((x, y))
        may = y

Z.append((mih, 10 ** 9))
for i in range(len(Z) - 1):
    ans = min(ans, (Z[i][1] - Z[i+1][0]) * (mah - mil))
print(ans)
