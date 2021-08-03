# cook your dish here
import sys


def LCM(a, b):
    lar = max(a, b)
    small = min(a, b)
    i = lar
    while(1):
        if (i % small == 0):
            return i
        i += lar


for _ in range(int(input())):
    M, N = map(int, input().split())
    print(LCM(M, N))
