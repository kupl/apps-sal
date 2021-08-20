import math
for _ in range(int(input())):
    (c, d) = list(map(int, input().split()))
    size = int(math.sqrt(c * d))
    while size > 0:
        if c * d % (size * size) == 0:
            k = c * d / (size * size)
            if c % size == 0 and d % size == 0:
                print(int(k))
                break
        size -= 1
