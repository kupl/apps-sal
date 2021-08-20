import math
t = int(input())
for i in range(t):
    n = int(input())
    (num, x, y, count) = (1, 0, 0, 0)
    while num * num > y and num <= n:
        y = y + num * num
        x = num
        count += 1
        num = math.floor(math.sqrt(y)) + 1
    print(count)
