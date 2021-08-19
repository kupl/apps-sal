# cook your dish here
from math import ceil
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(ceil(n / min(a)))
