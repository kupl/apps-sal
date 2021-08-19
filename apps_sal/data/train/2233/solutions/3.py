from collections import defaultdict
from functools import reduce
from types import GeneratorType
from sys import stderr
from fractions import Fraction
import sys
import os
from io import BytesIO, IOBase
from itertools import *
import bisect
from heapq import *
from math import ceil, floor
from copy import *
from collections import deque, defaultdict
from collections import Counter as counter
from itertools import combinations
from itertools import permutations as permutate
from bisect import bisect_left as bl
from operator import *
from bisect import bisect_right as br
from bisect import bisect
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            (self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            (self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            (self.buffer.truncate(0), self.buffer.seek(0))


class IOWrapper(IOBase):

    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    (sep, file) = (kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout))
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False):
        file.flush()


if sys.version_info[0] < 3:
    (sys.stdin, sys.stdout) = (FastIO(sys.stdin), FastIO(sys.stdout))
else:
    (sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))


def iterative(f, stack=[]):

    def wrapped_func(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
                continue
            stack.pop()
            if not stack:
                break
            to = stack[-1].send(to)
        return to
    return wrapped_func


mod = 1000000007


def inp():
    return sys.stdin.readline().rstrip('\r\n')


def out(var):
    sys.stdout.write(str(var))


def lis():
    return list(map(int, inp().split()))


def stringlis():
    return list(map(str, inp().split()))


def sep():
    return list(map(int, inp().split()))


def strsep():
    return list(map(str, inp().split()))


def fsep():
    return list(map(float, inp().split()))


def nextline():
    out('\n')


def testcase(t):
    for p in range(t):
        solve()


def pow(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if y & 1 == 1:
            res = res * x % p
        y = y >> 1
        x = x * x % p
    return res


def factors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def gcd(a, b):
    if a == b:
        return a
    while b > 0:
        (a, b) = (b, a % b)
    return a


def prefix_sum(ar):
    return list(accumulate(ar))


def suffix_sum(ar):
    return list(accumulate(ar[::-1]))[::-1]


def N():
    return int(inp())


def numberOfSetBits(i):
    i = i - (i >> 1 & 1431655765)
    i = (i & 858993459) + (i >> 2 & 858993459)
    return ((i + (i >> 4) & 252645135) * 16843009 & 4294967295) >> 24


def solve():
    n = N()
    ar = lis()
    for i in range(len(ar)):
        m = ar[i]
        v = m // 2
        u = v // 2
        w = v - u
        print((u * w + u + w + 1) % mod)


solve()
