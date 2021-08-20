for _ in range(int(input())):
    S = input()
    n = len(S)
    A = [0] * 26
    for i in S:
        A[ord(i) - 65] += 1
    A.sort()
    A = A[::-1]
    res = n
    for i in range(min(n, 26)):
        if n % (i + 1) == 0:
            F = n // (i + 1)
            y = 0
            for j in range(i + 1):
                y += min(A[j], F)
            res = min(res, n - y)
    print(res)
