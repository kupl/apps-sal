"""
Created on 6 mai 2012

@author: Quentin
"""
import sys


def readInput(stream):
    T = int(sys.stdin.readline())
    Ns = []
    for Tit in range(T):
        Ns.append(int(sys.stdin.readline()))
    return Ns


def isInt(myInt):
    return myInt - int(myInt) == 0.0


def getMaxFour(N):
    b = 1000.0
    a = -1.0
    while b > 0.0:
        a = a + 1.0
        b = (N - 4.0 * a) / 7.0
        if isInt(b):
            return int(b * 7)
    return -1


def __starting_point():
    Ns = readInput(sys.stdin)
    for N in Ns:
        slevin = getMaxFour(N)
        print(slevin)


__starting_point()
