import atexit
import io
import sys
import math
from collections import defaultdict, Counter
m = pow(10, 9) + 7
t = int(input())
l = [0] * 100001
l[1] = 1
for i in range(2, 100001):
    l[i] = i * l[i - 1] % m * (2 * i - 1) % m
for i in range(t):
    n = int(input())
    print(l[n])
