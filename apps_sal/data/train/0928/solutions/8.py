# cook your dish here
from math import sqrt
t=int(input())
for _ in range(t):
    n=int(input())
    rad=int(sqrt(n))
    div = rad//3
    print(rad-div)
