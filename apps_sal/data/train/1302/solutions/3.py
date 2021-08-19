# cook your dish here
from math import floor, sqrt
for _ in range(int(input())):
    n = int(input())
    y = n / 2
    x = floor(sqrt(y))
    print(x * 2)
