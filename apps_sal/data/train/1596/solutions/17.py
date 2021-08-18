import math


def Log2(x):
    return (math.log10(x) /
            math.log10(2))


def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))


t = int(input())
for i in range(t):
    x, y = list(map(int, input().split()))
    step_x = 0
    step_y = 0
    if(isPowerOfTwo(x + 1)):
        step_x = 1
    else:
        while(x >= 0):
            nx = Log2(x + 1)
            s = int(nx)
            x -= (2**s)
            step_x += 1
    if(isPowerOfTwo(y + 1)):
        step_y = 1
    else:
        while(y >= 0):
            ny = Log2(y + 1)
            s_y = int(ny)
            y -= (2**s_y)
            step_y += 1
    if(step_x == step_y):
        print(0, 0)
    elif(step_x > step_y):
        print(2, abs(step_x - step_y))

    else:
        print(1, abs(step_x - step_y))
