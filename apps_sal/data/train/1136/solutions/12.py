# cook your dish here
import math
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    n = math.ceil(n / 2)
    print(n * k)
