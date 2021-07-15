#!/usr/bin/env python3
# coding: utf-8
#Last Modified: 23/Feb/20 12:23:37 PM


import sys


def main():
    def checkValidity(a, b, c):   
        if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
            return False
        else: 
            return True      
    def checkrt(a, b, c):
        if a**2 + b**2 == c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
            return True
        return False
    for tc in range(int(input())):
        a, b, c=get_ints()
        if checkValidity(a, b, c):
            if checkrt(a, b, c):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')


get_array = lambda: list(map(int, sys.stdin.readline().split()))


get_ints = lambda: list(map(int, sys.stdin.readline().split()))


input = lambda: sys.stdin.readline().strip()


main()

