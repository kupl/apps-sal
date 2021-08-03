T = int(input())
for _ in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    X = int(input())
    A = l[:]
    B = l[:]
    for i in range(1, N):
        A[i] = A[i - 1] + A[i]
        B[N - 1 - i] = B[N - 1 - i] + B[N - i]
    # print(A,B)
    i = 0
    j = N - 1
    while i < j and j - i > 1:
        if A[i] / X < B[j]:
            i += 1
        elif A[i] / X > B[j]:
            j -= 1
        else:
            if i + 1 < N - j:
                j -= 1
            else:
                i += 1
    print(i + 1, N - j)
