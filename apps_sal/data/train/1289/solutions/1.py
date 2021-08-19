"""
from sys import stderr

def f(maxG, remaining):
    #stderr.write('%s %s
' % (maxG, remaining))
    if not remaining: return 1
    S = 0
    for i in xrange(len(remaining)):
     if remaining[i] < maxG:
     S += 2 * f(maxG, remaining[:i] + remaining[i+1:])
     else:
     S += 1 * f(remaining[i], remaining[:i] + remaining[i+1:])
    return S
"""


def process(N):
    P = 1
    for i in range(1, 2 * N, 2):
        P *= i
    return P


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        print(process(N))


main()
