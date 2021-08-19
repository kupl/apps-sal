import math
for _ in range(int(input())):
    N = int(input())
    count = 0
    while N > 0:
        n = int(math.sqrt(N))
        N = N - n ** 2
        count = count + 1
    print(count)
