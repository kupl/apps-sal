import math
p = [int(i) for i in input().split()]
count = 0
for i in range(1, p[0] + 1):
    for j in range(1, p[1] + 1):
        k = i * i + j
        k1 = int(math.sqrt(k))
        if k1 * k1 == k:
            count += 1
print(count)
