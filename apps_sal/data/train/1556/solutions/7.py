from sys import *
input = stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    l = [1 for _ in range(k)]
    for i in range(1, k):
        if l[i - 1] == 0:
            l[i] = 1
        else:
            l[i] = 0
    ans = ''.join([str(x) for x in l])
    for i in range(k):
        print(ans)
