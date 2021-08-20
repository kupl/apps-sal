import math
for _ in range(int(input())):
    (x1, y1, x2, y2) = list(map(int, input().split()))
    if math.sqrt(pow(x1, 2) + pow(y1, 2)) < math.sqrt(pow(x2, 2) + pow(y2, 2)):
        print('A IS CLOSER')
    else:
        print('B IS CLOSER')
