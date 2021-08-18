try:
    from math import sqrt
    for _ in range(int(input())):
        floor, vel1, vel2 = map(int, input().rstrip().split())
        if (sqrt(2) * floor) / vel1 < (2 * floor) / vel2:
            print('Stairs')
        else:
            print('Elevator')
except:
    pass
