for _ in range(int(input())):
    A = list(map(int, input().split()))
    p = A[5]
    del A[5]
    if 24 * 5 < p * sum(A):
        print('Yes')
    else:
        print('No')
