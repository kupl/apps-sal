import sys
sys.setrecursionlimit(10 ** 5 + 1)
inf = int(10 ** 20)
max_val = inf
min_val = -inf


def RW():
    return sys.stdin.readline().strip()


def RI():
    return int(RW())


def RMI():
    return [int(x) for x in sys.stdin.readline().strip().split()]


def RWI():
    return [x for x in sys.stdin.readline().strip().split()]


MOD = 998244353
for _ in [0] * RI():
    (lenA, lenB) = RMI()
    arrA = RMI()
    arrB = RMI()
    (sumA, sumB) = (sum(arrA), sum(arrB))
    for _ in [0] * RI():
        (mode, *param) = RMI()
        if mode == 3:
            print(sumA % MOD * (sumB % MOD) % MOD)
        else:

            def adds():
                (a, b, c) = param
                return c * (b - a + 1)
            if mode == 1:
                sumA += adds()
            else:
                sumB += adds()
