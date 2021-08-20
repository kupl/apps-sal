from math import log2, floor
for _ in range(int(input())):
    (x, y) = list(map(int, input().split()))
    (count1, count2) = (0, 0)
    while True:
        z = floor(log2(x + 1))
        x = x - (2 ** z - 1)
        x -= 1
        count1 += 1
        if x < 0:
            break
    while True:
        z = floor(log2(y + 1))
        y = y - (2 ** z - 1)
        y -= 1
        count2 += 1
        if y < 0:
            break
    if count1 == count2:
        print(0, 0)
    if count1 > count2:
        print(2, abs(count1 - count2))
    if count2 > count1:
        print(1, count2 - count1)
