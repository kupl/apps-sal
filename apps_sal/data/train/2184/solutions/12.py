import itertools
import sys

def __starting_point():
    n, q = map(int, input().split())
    blocks = list(map(int, input().split()))
    # create empty dictionary - unordered collection
    dif = dict()

    for i in range(n):
        if blocks[i] in dif:
            dif[blocks[i]][1] = i
            dif[blocks[i]][2] = dif[blocks[i]][2] + 1
        elif blocks[i] not in dif:
            dif[blocks[i]] = [i, i, 1]

    rez = 0
    end = -1
    maxi = -1
    for i in range(n):
        if dif[blocks[i]][1] >= end:
            end = dif[blocks[i]][1]
        if dif[blocks[i]][2] >= maxi:
            maxi = dif[blocks[i]][2]
        if i == end:
            rez  = rez + maxi
            maxi = 0
    rez = (-1) * rez
    for i in dif:
        rez = rez + dif[i][2]
    print(rez)
__starting_point()
