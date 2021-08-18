import math
n = int(input())

for i in range(0, n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    loga = int(math.log(a, 2))
    logb = int(math.log(b, 2))

    dist = 0

    while loga > logb:
        a = a / 2
        dist += 1
        loga -= 1

    while loga < logb:
        b = b / 2
        dist += 1
        logb -= 1

    while a != b:
        a = a / 2
        b = b / 2
        dist += 2

    print(dist)
