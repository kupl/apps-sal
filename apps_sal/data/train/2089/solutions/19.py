from sys import *
d = {'|': lambda t: t | k, '&': lambda t: t & k, '^': lambda t: t ^ k}
 
a, b = 1023, 0
for i in range(int(input())):
    s, q = stdin.readline().split()
    k = int(q)
    a = d[s](a)
    b = d[s](b)
 
t = [2]
for u in range(1024):
    for v in range(1024):
        if 1023 ^ v == a and u ^ v == b:
            print('2\n|', u, '\n^', v)
            return
