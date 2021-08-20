from collections import *
n = int(input())
s = list(map(int, input().split()))
x = max(Counter(s).values())
print(n - x)
