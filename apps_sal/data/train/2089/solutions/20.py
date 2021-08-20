import os
import sys
from io import BytesIO, IOBase
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


(sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))


def input():
    return sys.stdin.readline().rstrip('\r\n')


a = int(input())
bits = ['r' for i in range(10)]
temp = ['r' for i in range(10)]
for i in range(a):
    (x, y) = input().split()
    y = int(y)
    n = bin(y)
    n = n[2:]
    ans = ''
    for i in range(10 - len(n)):
        ans += '0'
    ans = ans + n
    if x == '|':
        for i in range(len(bits)):
            if ans[i] == '1':
                temp[i] = '1'
    if x == '&':
        for i in range(len(bits)):
            if ans[i] == '0':
                temp[i] = '0'
    if x == '^':
        for i in range(len(bits)):
            if temp[i] == '0' and ans[i] == '1' or (temp[i] == '1' and ans[i] == '0'):
                temp[i] = '1'
            elif temp[i] == ans[i] and (temp[i] == '0' or temp[i] == '1'):
                temp[i] = '0'
            elif ans[i] == '1':
                if temp[i] == 'r':
                    temp[i] = 'rb'
                else:
                    temp[i] = 'r'
ad = ['0' for i in range(10)]
xor = ['0' for i in range(10)]
nd = ['1' for i in range(10)]
for i in range(len(temp)):
    if temp[i] == '1':
        ad[i] = '1'
        nd[i] = '1'
        xor[i] = '0'
    elif temp[i] == '0':
        nd[i] = '0'
        ad[i] = '0'
        xor[i] = '1'
    elif temp[i] == 'rb':
        xor[i] = '1'
        ad[i] = '0'
        nd[i] = '1'
    else:
        xor[i] = '0'
        ad[i] = '0'
        nd[i] = '1'
ad = int(''.join(map(str, ad)), 2)
nd = int(''.join(map(str, nd)), 2)
xor = int(''.join(map(str, xor)), 2)
print(3)
print('^', xor)
print('&', nd)
print('|', ad)
