import math
t = int(input())
while(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(math.ceil(n / min(arr)))

    t -= 1
