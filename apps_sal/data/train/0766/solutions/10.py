from sys import *
input = stdin.readline
for u in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    print(l[-1] * l[-2], l[0] * l[1])
