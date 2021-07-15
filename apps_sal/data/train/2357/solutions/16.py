import sys


class IO:
    @staticmethod
    def get(type=str):
        return type(input().strip())
    
    @staticmethod
    def gets(type=str):
        return [type(x) for x in input().split()]


def printerr(*args, **kw):
    print(*args, **kw, file=sys.stderr)


def inv(n, p):
    return pow(n, p-2, p)

def comb(n, k, p):
    k = min(k, n-k)
    t, d = 1, 1
    for i in range(k):
        t *= n - i
        t %= P
        d *= i+1
        d %= P
    return t * inv(d, P) % P


P = 10 ** 9 + 7

def main():
    n, m = IO.gets(int)
    a = IO.gets(int)

    x = sum(a) + n
    dm = m - sum(a)
    printerr(f"x={x} dm={dm}")

    if dm < 0:
        ans = 0
    elif dm == 0:
        ans = 1
    else:
        # ans = (1 - pow(x, m+1, P)) * inv(1 - x, P) % P
        ans = comb(x+dm, dm, P)

    print(ans)


def __starting_point():
    main()
__starting_point()
