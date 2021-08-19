import sys
from random import choice, randint
inp = sys.stdin.readline
out = sys.stdout.write
flsh = sys.stdout.flush
sys.setrecursionlimit(10 ** 9)
inf = 10 ** 20
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def MI():
    return map(int, inp().strip().split())


def LI():
    return list(map(int, inp().strip().split()))


def LLI():
    return [list(map(int, l.split())) for l in sys.stdin.readlines().strip()]


def LI_():
    return [int(x) - 1 for x in inp().strip().split()]


def LF():
    return [float(x) for x in inp().strip().split()]


def LS():
    return inp().strip().split()


def I():
    return int(inp().strip())


def F():
    return float(inp().strip())


def S():
    return inp().strip()


def pf(s):
    return out(s + '\n')


def JA(a, sep):
    return sep.join(map(str, a))


def JAA(a, s, t):
    return s.join((t.join(map(str, b)) for b in a))


def main():
    from math import ceil
    t = I()
    l = []
    for _ in range(t):
        (n, k) = MI()
        if n == 0:
            k -= 1
            ans = k * (k + 1) % mod
            l.append(ans)
        elif k % 2 != 0:
            lr = k // 2
            l.append((n * n % mod + lr * (2 * n % mod) % mod + lr * (lr + 1) % mod) % mod)
        else:
            lr = k // 2
            l.append((n * n % mod + lr * (2 * n) % mod % mod + lr * (lr - 1) % mod) % mod)
    for i in range(t):
        pf(str(l[i]))


def __starting_point():
    main()


__starting_point()
