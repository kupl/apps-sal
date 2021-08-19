from sys import *
input = stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    num = 1
    diff = 1
    for i in range(n):
        y = num
        for j in range(i + 1):
            print(y, end='')
            y -= 1
        diff = diff + 1
        num += diff
        print()
