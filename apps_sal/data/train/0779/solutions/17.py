for i in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    A = A[::-1]
    x = (A[0] + A[1]) / 2
    if len(A) > 2:
        for i in range(2, len(A)):
            x = (A[i] + x) / 2
    print('%.6f' % x)
