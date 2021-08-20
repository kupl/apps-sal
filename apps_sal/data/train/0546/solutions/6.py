import math
t = int(input())
for i in range(t):
    k = int(input())
    count = 0
    temp = int(math.log2(k))
    for j in range(temp, -1, -1):
        if k - 2 ** j >= 0:
            k = k - 2 ** j
            count = count + 1
    print(count - 1)
