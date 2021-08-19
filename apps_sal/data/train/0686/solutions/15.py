import math
T = int(input())
for i in range(T):
    data = input().split(' ')
    elev = int(data[0])
    str = math.sqrt(2) * int(data[0])
    if str * int(data[1]) > elev * int(data[2]):
        print('Stairs')
    else:
        print('Elevator')
