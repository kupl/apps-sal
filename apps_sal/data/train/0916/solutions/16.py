# cook your dish here
from math import gcd


def cakes(a, b):
    print(int(a * b / gcd(a, b)))


for _ in range(int(input())):
    cakes(*list(map(int, input().split())))
