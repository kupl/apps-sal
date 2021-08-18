import math
for h in range(int(input())):
    f, d, t, b = map(int, input().split())
    tg = math.sqrt(2 * (f + d) / t)
    bl = f / b
    if tg <= bl:
        print('Tiger')
    else:
        print('Bolt')
