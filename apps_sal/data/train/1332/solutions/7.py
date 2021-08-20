import math
n = int(input())
for i in range(0, n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    loga = int(math.log(a, 2))
    logb = int(math.log(b, 2))
    dist = 0
    if loga > logb:
        dist += loga - logb
        a = a >> loga - logb
    else:
        b = b >> logb - loga
        dist += logb - loga
    x = a ^ b
    if x:
        dist += (int(math.log(x, 2)) + 1) * 2
    print(dist)
