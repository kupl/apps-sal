import math
t = int(input())
while t > 0:
    n, l = list(map(int, input().split()))
    if n == 1:
        print(l)
    elif n == 2:
        for i in range(1, 101):
            if l // i == 2:
                print(i)
                break

    t -= 1
