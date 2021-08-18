import math
for _ in range(int(input())):
    n, k = [int(j) for j in input().split()]
    l = list(map(int, input().split()))
    sum = l[0]
    for i in range(n - 1):
        if i % 2 == 0:
            if sum >= 0:
                sum -= l[i + 1]
            else:
                sum += l[i + 1]
        else:
            if sum >= 0:
                sum += l[i + 1]
            else:
                sum -= l[i + 1]
    if math.fabs(sum) >= k:
        print("1")
    else:
        print("2")
