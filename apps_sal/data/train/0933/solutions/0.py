#!/usr/bin/env python2

def gc(c):
    return 'a' <= c <= 'h'


def gd(c):
    return '1' <= c <= '8'


t = int(input())
for i in range(t):
    line = input()
    if len(line) != 5:
        print("Error")
        continue
    if line[2] != '-':
        print("Error")
        continue
    x1 = line[0]
    y1 = line[1]
    x2 = line[3]
    y2 = line[4]
    if gc(x1) and gd(y1) and gc(x2) and gd(y2):
        d1 = abs(ord(x1) - ord(x2))
        d2 = abs(ord(y1) - ord(y2))
        if d1 > d2:
            d1, d2 = d2, d1
        if (d1 == 1) and (d2 == 2):
            print("Yes")
        else:
            print("No")
    else:
        print("Error")
