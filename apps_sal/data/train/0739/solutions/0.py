#!/usr/bin/env python

from math import sqrt


def process(S):
    P = [0, 0, 'S']
    for i in S:
        if i == 'L':
            if P[-1] == 'N':
                P[-1] = 'W'
            elif P[-1] == 'S':
                P[-1] = 'E'
            elif P[-1] == 'E':
                P[-1] = 'N'
            elif P[-1] == 'W':
                P[-1] = 'S'
        elif i == 'R':
            if P[-1] == 'N':
                P[-1] = 'E'
            elif P[-1] == 'S':
                P[-1] = 'W'
            elif P[-1] == 'E':
                P[-1] = 'S'
            elif P[-1] == 'W':
                P[-1] = 'N'
        else:
            i = int(i)
            if P[-1] == 'N':
                P[1] -= i
            elif P[-1] == 'S':
                P[1] += i
            elif P[-1] == 'E':
                P[0] += i
            elif P[-1] == 'W':
                P[0] -= i
        # print i, P
    DIST = sqrt(P[0]**2 + P[1]**2)

    if P[0] == 0 and P[1] == 0:
        DIR = ''
    elif P[0] == 0 and P[1] < 0:
        DIR = 'S'
    elif P[0] == 0 and P[1] > 0:
        DIR = 'N'
    elif P[0] < 0 and P[1] == 0:
        DIR = 'E'
    elif P[0] < 0 and P[1] < 0:
        DIR = 'SE'
    elif P[0] < 0 and P[1] > 0:
        DIR = 'NE'
    elif P[0] > 0 and P[1] == 0:
        DIR = 'W'
    elif P[0] > 0 and P[1] < 0:
        DIR = 'SW'
    elif P[0] > 0 and P[1] > 0:
        DIR = 'NW'

    DIST = int(DIST * 10.) / 10.  # TOLD NO APPROXIMATION

    return '%.1f%s' % (DIST, DIR)


def main():
    T = int(input())
    for t in range(T):
        S = input().split()
        print(process(S))


main()
