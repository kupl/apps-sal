from sys import stdin, stdout
from math import log2
n = int(stdin.readline())
challengers = []
for i in range(n):
    (a, b, c, d) = map(int, stdin.readline().split())
    challengers.append((-(a + b + c + d), i))
challengers.sort()
for i in range(n):
    if not challengers[i][1]:
        stdout.write(str(i + 1))
        break
