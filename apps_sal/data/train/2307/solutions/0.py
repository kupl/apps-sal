import sys
stdin = sys.stdin


def ip():
    return int(sp())


def fp():
    return float(sp())


def lp():
    return list(map(int, stdin.readline().split()))


def sp():
    return stdin.readline().rstrip()


def yp():
    return print('Yes')


def np():
    return print('No')


(n, a, b) = lp()
x = lp()
ans = 0
for i in range(n - 1):
    ans += min(b, a * (x[i + 1] - x[i]))
print(ans)
