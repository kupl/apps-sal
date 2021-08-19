"""
Created on 22-Nov-2015

@author: root1
"""
from fractions import gcd


def read_int():
    return int(input())


def read_int_list():
    return [int(x) for x in input().split()]


def __gcd(lst):
    result = 0
    for num in lst:
        result = gcd(result, num)
    return result


def main():
    tc = read_int()
    for _ in range(tc):
        n = read_int()
        print(n * __gcd(read_int_list()))


def __starting_point():
    main()


__starting_point()
