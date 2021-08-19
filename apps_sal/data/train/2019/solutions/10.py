__author__ = 'Alex'
import math
n = int(input())
a = list(map(int, input().split()))
asum = sum(a)
first = math.ceil(asum / (n - 1))
print(max(first, max(a)))
