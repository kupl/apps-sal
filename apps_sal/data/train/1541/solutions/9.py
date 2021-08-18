import math
for i in range(int(input())):
    n = int(input())
    bound = [int(i) for i in input().split()]
    ball = [int(i) for i in input().split()]
    speed = [int(i) for i in input().split()]
    chef = [int(i) for i in input().split()]
    cspeed = 0
    time = float('inf')
    for i in range(n):
        if(speed[i] > 0):
            a = (bound[i] - ball[i]) / speed[i]
            time = min(a, time)
        elif(speed[i] < 0):
            a = abs(ball[i] / speed[i])
            time = min(a, time)

    a = b = c = 0
    for i in range(n):
        c += speed[i]**2
        a += (ball[i] - chef[i])**2
        b += 2 * speed[i] * (ball[i] - chef[i])
    if(a == 0):
        print(0)
    else:
        x = -b / (2 * a)
        if(x >= 1 / time):
            cspeed = c - (b**2) / (4 * a)
            print(math.sqrt(cspeed))
        else:
            cspeed = a / (time**2) + b / time + c
            print(math.sqrt(cspeed))
