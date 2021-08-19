import math
for i in range(int(input())):
    (m, n) = list(map(int, input().split()))
    val = math.floor(math.log10(n + 1))
    print(m * val, end=' ')
    if val != 0:
        print(m)
    else:
        print(0)
