import math
x = int(input())
y = list(map(int, input().split(' ')))
print(max(max(y), math.ceil(sum(y) / (x - 1))))
