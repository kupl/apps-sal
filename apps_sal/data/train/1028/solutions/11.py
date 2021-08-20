import math
for _ in range(int(input())):
    N = int(input())
    D = math.floor(math.log(N, 10)) + 1
    T = N
    R = 0
    while T > 0:
        M = T % 10
        T = T // 10
        R += pow(M, D)
    if R == N:
        print('FEELS GOOD')
    else:
        print('FEELS BAD')
