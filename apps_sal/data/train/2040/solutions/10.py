#!/usr/bin/env python3
from sys import stdin, stdout
from decimal import Decimal


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n, h = rint()

As = Decimal(h) / Decimal(2 * n)
x = []
for i in range(1, n):
    x.append(Decimal(i * As * 2 * h).sqrt())

print(*x)
