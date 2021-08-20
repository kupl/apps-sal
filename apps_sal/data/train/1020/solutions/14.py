import math
T = int(input())
for j in range(T):
    (N, K) = [int(j) for j in input().split()]
    s = list(map(int, input().split()))
    sum = s[0]
    for i in range(N - 1):
        if i % 2 == 0:
            if sum >= 0:
                sum -= s[i + 1]
            else:
                sum += s[i + 1]
        elif sum >= 0:
            sum += s[i + 1]
        else:
            sum -= s[i + 1]
    if math.fabs(sum) >= K:
        print('1')
    else:
        print('2')
