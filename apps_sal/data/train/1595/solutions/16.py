import itertools
import numpy as np


def countBits(p1):
    count = 0
    p2 = p1
    while p2:
        p2 = p2 & p2 - 1
        count = count + 1
    p = '{0:b}'.format(p1)
    if count == len(p):
        return True
    else:
        return False


def __starting_point():
    t = eval(input())
    for i in range(t):
        s = input()
        n = eval(input())
        f_list = []
        for j in range(n):
            f_list.append(input())
        inp = ''
        bin_list = []
        for j in range(len(s)):
            if s[j] == 'w':
                inp = inp + '0'
            else:
                inp = inp + '1'
        for j in range(n):
            s1 = ''
            for k in range(len(f_list[j])):
                if f_list[j][k] == '+':
                    s1 = s1 + '1'
                else:
                    s1 = s1 + '0'
            bin_list.append(s1)
        lst = [list(k) for k in itertools.product([0, 1], repeat=n)]
        count = 0
        for j in range(len(lst)):
            p = '0' * n
            for k in range(len(lst[j])):
                if lst[j][k] == 1:
                    p1 = int(p, 2) ^ int(bin_list[k], 2)
                    p = '{0:b}'.format(p1)
            p2 = int(p, 2) ^ int(inp, 2)
            if p2 == 2 ** len(s) - 1:
                count = (count + 1) % (10 ** 9 + 7)
        print(count % (10 ** 9 + 7))


__starting_point()
