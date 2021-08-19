import atexit
import io
import sys
import math
from collections import defaultdict, Counter
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def isprime(d):
    for j in range(2, int(math.sqrt(d)) + 1):
        if d % j == 0:
            return False
    return True


m = 100000007
t = int(input())
for i in range(t):
    (n, k1, k2) = list(map(int, input().split()))
    (p1, p2, p3, p4) = list(map(int, input().split()))
    p = int(math.sqrt(k1))
    if p * p < k1:
        p += 1
    c = 0
    ans = 0
    while p * p <= k2:
        c += 1
        if p != 1 and isprime(p):
            ans = (ans + p1) % m
        else:
            ans = (ans + p2) % m
        p += 1
    ans = (ans + p3 * (k2 - k1 + 1 - c) % m) % m
    print(ans)
