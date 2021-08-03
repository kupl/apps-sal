from math import sqrt
t = int(input())
for _ in range(t):
    n = int(input())
    print(int(sqrt(n >> 1)) << 1)
