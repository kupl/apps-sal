import sys
import math
# sys.setrecursionlimit(100000000)
input = sys.stdin.readline

############ ---- USER DEFINED INPUT FUNCTIONS ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(list(map(int, input().split())))
################################################################
############ ---- THE ACTUAL CODE STARTS BELOW ---- ############


t = inp()
for _ in range(t):
    n = inp()
    k = inp()
    x = k % n
    y = n - x
    if x == 0:
        print(0)
    elif x == y:
        ans = 2 * x - 1
        print(ans)
    else:
        ans = min(x, y) * 2
        print(ans)
