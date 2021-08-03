import math
for _ in range(int(input())):
    n, d = list(map(int, input().split()))

    m = list(map(int, input().split()))
    risk = 0
    for i in range(len(m)):
        if 80 <= m[i] or m[i] <= 9:
            risk += 1
    print(math.ceil(risk / d) + math.ceil((n - risk) / d))
