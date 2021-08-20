from sys import *
input = stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    y = 1
    for i in range(n):
        y = i + 1
        for j in range(n):
            print(y, end='')
            y = y + 1
            if y > n:
                y = y % n
            if y == 0:
                y = 1
        print()
