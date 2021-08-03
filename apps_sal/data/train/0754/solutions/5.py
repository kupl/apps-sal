from sys import *
input = stdin.readline
for u in range(int(input())):
    num = int(input())
    while num > 0:
        r = num % 10
        # print(r)
        if r % 2 == 0:
            print(1)
            break
        num = num // 10
    else:
        print(0)
