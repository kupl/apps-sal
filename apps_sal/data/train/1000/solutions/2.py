import math
t = int(input())
while t:
    t = t - 1
    n = int(input())
    a = list(map(int, input().split()))
    print(math.ceil(n / min(a)))
