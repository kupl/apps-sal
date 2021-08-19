from sys import stdin, stdout
#from math import gcd as g
#a,b = map(int, stdin.readline().split())
#l1 = list(map(int, stdin.readline().split()))
l = [1, 6, 7]
c = 1
for x in range(3, 100001):
    if x % 2 == 1:
        a = l[c] * 6
        l.append(a)
    else:
        l.append(a + 1)
        c += 1
n = int(stdin.readline())
for _ in range(n):
    s = int(stdin.readline())
    print(l[s - 1])
