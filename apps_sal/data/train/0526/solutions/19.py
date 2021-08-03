# cook your dish here
from sys import stdin, stdout
import math
from itertools import permutations, combinations
from collections import defaultdict
from bisect import bisect_left
from bisect import bisect_right


def L():
    return list(map(int, stdin.readline().split()))


def In():
    return list(map(int, stdin.readline().split()))


def I():
    return int(stdin.readline())


P = 1000000007


def main():
    for t in range(I()):
        s = input()
        st = s[0]
        i = 1
        c1, c2 = 1, 0
        while i < len(s):
            if s[i] == s[i - 1]:
                j = i
                c = 0
                while j < len(s) and s[j] == s[i - 1]:
                    c += 1
                    j += 1
                if c != 0:
                    c2 += 1
                    i = j - 1
                    st += str(c + 1)
            else:
                st += s[i]
                c1 += 1
            i += 1
        print(len(s) * 8 - (c1 * 8 + c2 * 32))


def __starting_point():
    main()


__starting_point()
