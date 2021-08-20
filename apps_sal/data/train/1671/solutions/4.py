"""
#If FastIO not needed, use this and don't forget to strip
#import sys, math
#input = sys.stdin.readline
"""
import math
import string
from collections import defaultdict as dd, deque as dq, Counter as dc
import os
import sys
from io import BytesIO, IOBase
import heapq as h
from bisect import bisect_left, bisect_right
import time
from types import GeneratorType
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            (self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            (self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
            (self.buffer.truncate(0), self.buffer.seek(0))


class IOWrapper(IOBase):

    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


(sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))


def input():
    return sys.stdin.readline().rstrip('\r\n')


def getInts():
    return [int(s) for s in input().split()]


def getInt():
    return int(input())


def getStrs():
    return [s for s in input().split()]


def getStr():
    return input()


def listStr():
    return list(input())


def getMat(n):
    return [getInts() for _ in range(n)]


MOD = 10 ** 9 + 7
'\n\n'


def solve():
    N = getInt()
    ans = [1] * N
    print(*ans)
    return


for _ in range(getInt()):
    solve()
