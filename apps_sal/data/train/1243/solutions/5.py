from sys import *
input = stdin.readline
t = int(input())
for _ in range(t):
    s = list(input())
    n = s.count('0') + s.count('5')
    if n > 0:
        print('1')
    else:
        print('0')
