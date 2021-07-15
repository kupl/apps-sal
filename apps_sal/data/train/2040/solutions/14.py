from math import sqrt
n, h = map(int, input().split())
for i in range(1, n):
    print(sqrt(i/n)*h, end=' ')
print()

