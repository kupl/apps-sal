import math
for _ in range(int(input())):
    n = int(input())
    cameras = list(map(int, input().split()))
    p, q = map(int, input().split())
    cameras.sort()
    sumA = 0
    # radians  c**2 = a**2 + b**2 -2ac(Cos(degree))
    for i in range(n // 2):
        p1 = cameras[i]
        p2 = cameras[n - 1 - i]
        p12 = p2 - p1
        # print(p1,p2)
        sideA = math.sqrt((p - p1)**2 + q**2)
        sideB = math.sqrt((p - p2)**2 + q**2)
        # print('sideA:',sideA,'sideB:',sideB)
        radians = math.acos(((p12**2) - sideA**2 - sideB**2) / (-2 * sideA * sideB))
        sumA += radians

    print(sumA)
