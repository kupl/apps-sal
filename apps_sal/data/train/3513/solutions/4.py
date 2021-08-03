import sys
sys.setrecursionlimit(1500)


def folding(a, b, t=1):
    if a == b:
        return t
    else:
        t += 1
        return folding(min(a, b), abs(a - b), t)
