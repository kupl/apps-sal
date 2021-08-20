from bisect import bisect_left as bisect
from math import log


def isPrime(n):
    return n == 2 or (n % 2 and all((n % p for p in range(3, int(n ** 0.5) + 1, 2))))


MAX = 1500000
mPow2 = int(log(MAX, 2))
STONES = sorted((n for n in {2 ** n2 * 3 ** n3 + 1 for n2 in range(mPow2 + 1) for n3 in range(int(log(MAX // 2 ** n2, 3)) + 1)} if isPrime(n)))


def solve(x, y):
    low = bisect(STONES, x)
    return bisect(STONES, y, low, len(STONES)) - low
