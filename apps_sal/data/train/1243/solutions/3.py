from sys import *
input = stdin.readline
for i in range(int(input())):
    n = int(input())
    while n > 0:
        r = n % 10
        if r % 5 == 0:
            print(1)
            break
        n = n // 10
    else:
        print(0)
