import math
n = int(input())
a = list(map(int, input().split()))
s = math.ceil(sum(a) / (n - 1))
print(max(max(a), s))
