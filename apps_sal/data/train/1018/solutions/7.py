t = int(input())
for i in range(0, t):
    n = int(input())
    A = [int(x) for x in input().split()]
    if(n > 2):
        for i in range(0, n - 2):
            if(i == 0):
                result = min(A[i] - A[i + 1], A[i + 1] - A[i + 2])
            else:
                result = min(result, A[i + 1] - A[i + 2])
    else:
        result = A[0] - A[1]
    print(result)
