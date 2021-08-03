import math

n, h = map(int, input().split())
base = 1 / n
prev = base
print(h * math.sqrt(prev), end=' ')

for x in range(n - 2):
    curr = prev + base
    print(h * math.sqrt(curr), end=' ')
    prev = curr
