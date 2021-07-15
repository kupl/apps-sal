# -*- coding: utf-8 -*-

# Baqir Khan
# Software Engineer (Backend)

import bisect as b
from sys import stdin

inp = stdin.readline

pre_calc = x = [[] for i in range(10)]


def get_g(num):
    while num > 9:
        new_num = 1
        while num:
            digit = num % 10
            if digit:
                new_num *= digit
            num //= 10
        num = new_num
    return num


for i in range(1, 10 ** 6 + 5):
    pre_calc[get_g(i)].append(i)

q = int(inp())

while q:
    q -= 1
    l, r, x = list(map(int, inp().split()))
    index_l = b.bisect_left(pre_calc[x], l)
    if index_l < len(pre_calc[x]) and pre_calc[x][index_l] >= l:
        index_l -= 1
    index_r = b.bisect_left(pre_calc[x], r)
    if index_r < len(pre_calc[x]) and pre_calc[x][index_r] <= r:
        index_r += 1
    print(max(index_r - index_l - 1, 0))

