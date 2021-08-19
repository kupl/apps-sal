import sys


def input():
    return sys.stdin.readline()[:-1]


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    (a, b) = ('', '')
    one = False
    for i in range(n):
        if s[i] == '0':
            a += '0'
            b += '0'
        elif s[i] == '1':
            if not one:
                a += '1'
                b += '0'
                one = True
            else:
                a += '0'
                b += '1'
        elif not one:
            a += '1'
            b += '1'
        else:
            a += '0'
            b += '2'
    print(a)
    print(b)
