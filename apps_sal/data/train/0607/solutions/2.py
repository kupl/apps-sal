import math
T = int(input())
for i in range(T):
    N = int(input())
    lis = list(map(int, input().split()))
    count = 0
    temp = lis[0]
    for j in lis[1:]:
        if temp == 1:
            count += 1
            temp = j
        temp = math.gcd(temp, j)
    if temp == 1:
        count += 1
    print(count)
