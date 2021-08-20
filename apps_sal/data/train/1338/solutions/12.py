import math
l = list(map(float, input().split()))
for i in range(1, len(l), 2):
    k = l[i] * pow(10, l[i + 1])
    print('{:.2f}'.format(k))
