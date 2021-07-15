from math import sqrt

n, h = map(int, input().split(' '))

for i in range(1, n):
    r = h*sqrt(i/n)
    print(str(r), end=" ")
