import os
import sys
from io import BytesIO, IOBase
# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
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
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# ------------------------------
 
def RL(): return list(map(int, sys.stdin.readline().rstrip().split()))
def RLL(): return list(map(int, sys.stdin.readline().rstrip().split()))
def N(): return int(input())
def print_list(l):
    print(' '.join(map(str,l)))
# import sys
# sys.setrecursionlimit(5010)
# from heapq import *
# from collections import deque as dq
from math import ceil,floor,sqrt,pow
# import bisect as bs
# from collections import Counter
# from collections import defaultdict as dc 

def judgePrime(n):
    if n < 2:
        return []     
    else:
        output = [1] * n
        output[0],output[1] = 0,0
        for i in range(2,int(n**0.5)+1): 
            if output[i] == 1:
                output[i*i:n:i] = [0] * len(output[i*i:n:i])
    return output

prime = judgePrime(1000005)
s = [0]
for i in range(1,1000005):
    s.append(s[-1]+prime[i])

t = N()
a = RL()
for n in a:
    print(s[n]-s[int(sqrt(n))]+1)

