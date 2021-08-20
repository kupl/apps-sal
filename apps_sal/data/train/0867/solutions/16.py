import math
for t in range(int(input())):
    l = [int(i) for i in input().split(' ')]
    if l[0] > sum(l[1:]):
        print(1)
    else:
        print(math.ceil(sum(l[1:]) / l[0]))
