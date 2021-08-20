import sys


def binpow(a, n, p):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = res * a % p
        a = a * a % p
        n >>= 1
    return res


def main():
    result = []
    t = int(sys.stdin.readline())
    for line in sys.stdin.readlines():
        (p, q, b) = list(map(int, line.split()))
        for i in range(6):
            b = b * b % q
        result.extend(list('Finite\n' if p * b % q == 0 else list('Infinite\n')))
    sys.stdout.write(''.join(result))


main()
