from sys import stdin, stdout
from collections import Counter
n = int(stdin.readline())
#l = list(map(int, stdin.readline().split()))
#l = [int(stdin.readline()) for _ in range(n)]
#a, b = map(int, stdin.readline().split())
for _ in range(n):
    n1 = int(stdin.readline())
    if n1 == 1:
        print('*')
    else:
        a = n1 + (n1 - 1)
        s = 0
        for x in range(1, n1):
            if x == 1:
                print(' ' * (n1 - 1) + '*' + ' ' * (n1 - 1))
                s += 1
            else:
                print(' ' * (n1 - x) + '*' + ' ' * (s) + '*')
                s += 2
            # print()
        print('*' * (a))
