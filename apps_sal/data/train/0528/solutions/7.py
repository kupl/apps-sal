import math
for _ in range(int(input())):
    (n, l) = [int(i) for i in input().split()]
    if n == 1:
        print(l)
    else:
        print(math.floor(l / (n + 1)) + 1)
