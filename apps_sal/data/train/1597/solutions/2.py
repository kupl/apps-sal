import math
T = int(input())
for i in range(T):
    list = []
    (A, M) = input().split()
    A = int(A)
    M = int(M)
    L1 = M // A
    L2 = math.ceil(M / (A + 1))
    while L2 <= L1:
        N = L2
        if M - N * A != 0 and N % (M - N * A) == 0:
            list.append(L2)
        L2 += 1
    print(len(list))
    if len(list) > 0:
        for j in range(len(list) - 1):
            print(list[j], end=' ')
        print(list[len(list) - 1])
    else:
        print(' ')
