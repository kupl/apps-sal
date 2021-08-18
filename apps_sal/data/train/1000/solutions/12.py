from math import ceil
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    min1 = min(arr)
    x = ceil(n / min1)
    print(x)
