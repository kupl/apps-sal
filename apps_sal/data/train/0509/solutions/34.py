'''
Hey  why peeping here -_'_- ?
I believe on myself and I will achieve
this->author = Fuad Ashraful Mehmet, CSE ,University of Asia Pacific
Todo:
'''
from collections import deque
from itertools import groupby
import sys
input = sys.stdin.readline


def R(): return map(int, input().split())
def I(): return int(input())
def S(): return input().rstrip('\n')
def L(): return list(R())


def HalfDead():
    n, m = R()
    g = dict()
    for i in range(1, n + 1):
        g[i] = dict()

    for i in range(m):
        u, v, c = R()
        g[u][v] = c
        g[v][u] = c
    color = [0] * (n + 2)
    color[1] = 1

    dq = deque()
    dq.append(1)

    while dq:
        frm = dq.popleft()

        for to, c in g[frm].items():

            if color[to] == 0:
                if color[frm] != c:
                    color[to] = c
                else:
                    if c == n:
                        color[to] = 1
                    else:
                        color[to] = c + 1

                dq.append(to)

    for i in range(n):
        print(color[i + 1])
    return


def __starting_point():
    HalfDead()


__starting_point()
