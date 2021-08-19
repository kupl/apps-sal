import sys
import math


def Int():
    return int(input())


def Str():
    return input()


def Ints():
    return map(int, input().split(' '))


def int_arr():
    return list(map(int, input().strip().split(' ')))


def str_arr():
    return list(map(str, input().split(' ')))


def vsInput():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


(no_of_citizen, visits) = Ints()
citizen_lst = []
maxi = 0
for i in range(no_of_citizen + visits):
    a = Int()
    if a != -1:
        citizen_lst.append(a)
        if a > maxi:
            maxi = a
    else:
        print(maxi)
        citizen_lst.remove(maxi)
        maxi = max(citizen_lst)
