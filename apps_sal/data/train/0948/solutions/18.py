import math
p = [int(i) for i in input().split()]
count = 0
for i in range(1, p[0] + 1):
    k = i + 1
    while True:
        y = k * k - i * i
        if y >= 1 and y <= p[1]:
            count += 1
        else:
            break
        k = k + 1
print(count)
