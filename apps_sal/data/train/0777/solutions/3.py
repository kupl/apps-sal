from math import pi as p
for II_II in range(eval(input())):
    r1, h1, r2, h2 = list(map(float, input().split()))
    a1 = ((p * r1 * r1 * h1) / 3) + ((2 * p * r1 * r1 * r1) / 3)
    a2 = (p * r2 * r2 * h2)
    print('%.9f' % a1, '%.9f' % a2)
