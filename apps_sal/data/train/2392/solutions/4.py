# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
from collections import defaultdict
from collections import deque
import math
import copy

T = int(input())
#N = int(input())
#s1 = input()
#s2 = input()
#N,Q = [int(x) for x in stdin.readline().split()]
#arr = [int(x) for x in stdin.readline().split()]

for i in range(T):
    N, M = [int(x) for x in stdin.readline().split()]

    d = M % 10

    q = N // M

    tail = []

    t = 0
    while True:
        t = (t + d) % 10
        if t not in tail:
            tail.append(t)
        else:
            break

    L = len(tail)

    s = sum(tail)
    q2 = q // L
    r = q % L

    # print(q2,r)
    print(q2 * s + sum(tail[:r]))
