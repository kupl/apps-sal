import math
for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    diff = abs(a - b)
    count = 0
    for i in range(1, int(math.sqrt(diff)) + 1):
        if diff % i == 0:
            if i == diff // i:
                count += 1
            else:
                count += 2
    print(count)
