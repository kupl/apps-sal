'''
Created on 6 mai 2012

@author: Quentin
'''
import sys
import re


def readInput(stream):
    T = int(stream.readline())
    JSs = []
    for Tit in range(T):
        J = re.sub("[\n\s]*", "", stream.readline())
        S = re.sub("[\n\s]*", "", stream.readline())
        JSs.append((J, S))
    return JSs


def compute(JSs):
    for J, S in JSs:
        count = 0
        for char in S:
            if J.find(char) != -1:
                count += 1
        print(count)


def __starting_point():
    JSs = readInput(sys.stdin)
    compute(JSs)


__starting_point()
