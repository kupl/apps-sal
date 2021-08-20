import sys


def iinput():
    return int(input())


for _ in range(iinput()):
    s1 = set(input())
    s2 = set(input())
    if len(s1 & s2):
        print('Yes')
    else:
        print('No')
