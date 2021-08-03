for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    A = ['0']
    A.extend(input())
    A.extend(['0'])

    B = [0] * (N + 2)
    C = B.copy()

    for i, j in enumerate(A[1:], start=1):
        if j == '1':
            B[i] = B[i - 1] + 1

    A.reverse()

    for i, j in enumerate(A[1:], start=1):
        if j == '1':
            C[i] = C[i - 1] + 1

    A.reverse()
    C.reverse()

    i = 1
    j = K
    ans = 0
    while j <= N:
        ans = max(ans, K + B[i - 1] + C[j + 1])
        i += 1
        j += 1

    print(ans)
