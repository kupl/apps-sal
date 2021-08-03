from sys import *
input = stdin.readline
for u in range(int(input())):
    n = input()
    s = sorted(n, reverse=True)
    print(''.join(s))
