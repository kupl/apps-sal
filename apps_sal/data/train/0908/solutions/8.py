"""input
3
3
5
7
"""
from sys import stdin, stdout
from math import sqrt, floor, ceil, log
from collections import defaultdict, Counter


def read():
    return stdin.readline().rstrip()


def write(x):
    stdout.write(str(x))


def endl():
    write('\n')


(data, x) = ([1], 1)
while data[-1] <= 10 ** 9:
    x += 1
    data.append(x * (x + 1) / 2)
for T in range(int(read())):
    (n, c) = (int(read()), 0)
    for i in data:
        if i <= n:
            c += 1
        else:
            break
    write(c)
    endl()
