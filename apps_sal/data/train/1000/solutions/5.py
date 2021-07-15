# cook your dish here
from math import ceil
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    m = min(arr)
    print(ceil(n/m))
