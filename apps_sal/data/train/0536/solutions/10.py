import math
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    print(math.floor(x / n))
