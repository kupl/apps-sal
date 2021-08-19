import sys
T = int(input())
while T > 0:
    t = sys.stdin.readline().split()
    N = int(t[0])
    M = int(t[1])
    A = [i for i in range(1, N + 1)]
    A = A[M:] + A[0:M]
    count = 1
    flag = True
    i = A[0] - 1
    A[0] = -1 * A[0]
    while flag and count < N:
        if A[i] < 0:
            flag = False
        else:
            j = A[i] - 1
            A[i] = -1 * A[i]
            i = j
            count += 1
    if not flag:
        print('No', count)
    else:
        print('Yes')
    T = T - 1
