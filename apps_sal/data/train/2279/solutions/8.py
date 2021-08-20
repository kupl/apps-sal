"""
    Author - Satwik Tiwari .
    27th Sept , 2020  - Sunday
"""
from types import GeneratorType
from fractions import Fraction
import sys
import os
from io import BytesIO, IOBase
from heapq import *
from copy import deepcopy
from collections import deque
from bisect import bisect_left as bl
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


mod = 10 ** 9 + 7


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


def zerolist(n):
    return [0] * n


def nextline():
    out('\n')


def testcase(t):
    for pp in range(t):
        solve(pp)


def printlist(a):
    for p in range(0, len(a)):
        out(str(a[p]) + ' ')


def google(p):
    print('Case #' + str(p) + ': ', end='')


def lcm(a, b):
    return a * b // gcd(a, b)


def power(x, y, p):
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


def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(max(n - r, 1)))


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


ans = [0] * (10 ** 6 + 5)


def sieve(a):
    for i in range(3, 10 ** 6 + 5, 2):
        a[i] = 1
    for i in range(3, 10 ** 6 + 5, 2):
        for j in range(i * i, 10 ** 6 + 5, i):
            a[j] = 0
    a[2] = 1
    return a


a = [0] * (10 ** 6 + 6)
a = sieve(a)
primes = []
for i in range(10 ** 6 + 1):
    if a[i]:
        primes.append(i)
for i in primes:
    ans[i] += 1
    ans[min(10 ** 6 + 2, i * i)] -= 1
for i in range(2, 10 ** 6 + 1):
    ans[i] += ans[i - 1]


def solve(case):
    n = int(inp())
    aa = lis()
    print('\n'.join((str(ans[i] + 1) for i in aa)))


testcase(1)
