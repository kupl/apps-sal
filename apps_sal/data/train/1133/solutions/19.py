import math
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    y = 0
    for x in arr:
        y = math.gcd(x, y)
        if y == 1:
            break
    z = sum(arr)
    print(y, ' ', z // y)
    t -= 1
