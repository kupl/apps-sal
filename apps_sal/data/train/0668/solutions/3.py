def maxSumSubarray(B):
    import sys
    (currSum, maxSum) = (0, -(sys.maxsize - 1))
    for b in B:
        currSum += b
        if currSum > maxSum:
            maxSum = currSum
        if currSum < 0:
            currSum = 0
    return maxSum


def formB(A, K):
    B = [0 for _ in range(len(A) * K)]
    for i in range(len(A)):
        B[i] = A[i]
        (ti, j) = (i, 1)
        while j < K:
            B[ti + len(A)] = A[i]
            ti += len(A)
            j += 1
    return maxSumSubarray(B)


try:
    T = int(input())
except Exception as e:
    pass
else:
    while T >= 1:
        (N, K) = map(int, input().split())
        A = [int(x) for x in input().split()]
        print(formB(A, K))
        T -= 1
