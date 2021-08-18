

import fractions
import sys

import pprint

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")

MOD = 10**9 + 7
IMG_SPACE = 2**10


def str2num(s, one_char):
    n = 0
    for ch in s:
        n = n << 1
        if ch == one_char:
            n = n | 1
    return n


def img2num(img_str):
    return str2num(img_str, 'w')


def flt2num(flt_str):
    return str2num(flt_str, '+')


def calc(S, filters_str):
    N = len(filters_str)
    img_num = img2num(S)
    filters_num = [flt2num(flt) for flt in filters_str]

    counts = [[0] * IMG_SPACE for i in range(N)]

    row = counts[N - 1]
    for i in range(IMG_SPACE):
        n = 0
        if i == 0:
            n += 1
        if i ^ filters_num[N - 1] == 0:
            n += 1
        row[i] = n

    for j in range(N - 2, -1, -1):
        row = counts[j]
        next_row = counts[j + 1]
        for i in range(IMG_SPACE):
            row[i] = (next_row[i] + next_row[i ^ filters_num[j]]) % MOD

    return counts[0][img_num]


T = int(f.readline().strip())

for case_id in range(1, T + 1):
    S = f.readline().strip()
    N = int(f.readline().strip())
    filters = []
    for i in range(N):
        filters.append(f.readline().strip())

    r = calc(S, filters)

    print(r)
