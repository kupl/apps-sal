import math
test = int(input())
for _ in range(test):
    last = int(input())
    x = 0
    y = 0
    c = 0
    while True:
        if y >= last * last:
            print(c)
            break
        c += 1
        x = int(math.sqrt(y)) + 1
        y = y + x * x
