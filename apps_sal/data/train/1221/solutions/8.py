from math import ceil

for i in range(int(input())):
    xf = int(input())
    x = 0
    y = 0
    p = 1
    step = 0
    while(x <= xf):
        x = p
        y += (p * p)
        p = ceil(y**0.5)
        step += 1
    print(step - 2)
