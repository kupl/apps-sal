import io
import os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def ii():
    return int(input())


def kk():
    return map(int, input().split())


def ll():
    return list(kk())


arr = [2] * 10
for _ in range(ii()):
    (s, v) = input().split()
    v = int(v)
    if s == b'|':
        for i in range(10):
            if v & 2 ** i:
                arr[i] = 1
    elif s == b'^':
        for i in range(10):
            if v & 2 ** i:
                arr[i] ^= 1
    elif s == b'&':
        for i in range(10):
            if not v & 2 ** i:
                arr[i] = 0
    else:
        print(s)
print(3)
x = o = a = 0
for i in range(10):
    if arr[i] == 3:
        x += 2 ** i
    elif arr[i] == 0:
        a += 2 ** i
    elif arr[i] == 1:
        o += 2 ** i
print('|', o)
print('^', x)
print('&', 2 ** 10 - a - 1)
