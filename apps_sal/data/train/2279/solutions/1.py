import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")

"""
New numbers are only lonely if prime.
When does a prime stop being lonely

"""


def get_p(n):
    """ Returns  a list of primes < n """
    z = int(n**0.5) + 1
    for s in range(4, len(sieve), 2):
        sieve[s] = False
    for i in range(3, z, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
            if i <= 1000:
                sq_primes.add(i * i)
    return


lim = 10**6
sieve = [True] * (lim + 1)
sq_primes = set()
sq_primes.add(4)
get_p(lim + 1)
ans = [0, 1]
for i in range(2, 10**6 + 1):
    tmp = ans[-1]
    if sieve[i]:
        tmp += 1
    elif i in sq_primes:
        tmp -= 1
    ans.append(tmp)


def solve():
    T = int(input().strip())
    A = [int(s) for s in input().split()]
    print(*[ans[A[j]] for j in range(T)])
    return


solve()
