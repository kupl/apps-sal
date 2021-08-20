import math
for i in range(int(input())):
    (s, d, a, b) = map(float, input().split())
    distance = s + d
    tiger = math.sqrt(2 * distance / a)
    bolt = s / b
    if tiger <= bolt:
        print('Tiger')
    else:
        print('Bolt')
