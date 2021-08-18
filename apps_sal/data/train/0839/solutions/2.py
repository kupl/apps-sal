def isSubsetSum(set, n, sum):
    subset = ([[False for i in range(sum + 1)]
               for i in range(n + 1)])

    for i in range(n + 1):
        subset[i][0] = True

    for i in range(1, sum + 1):
        subset[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i - 1]:
                subset[i][j] = subset[i - 1][j]
            if j >= set[i - 1]:
                subset[i][j] = (subset[i - 1][j]
                                or subset[i - 1][j - set[i - 1]])

    return subset[n][sum]


for _ in range(int(input())):
    K = int(input())
    N = int(input())
    array = list(map(int, input().split()))
    if K > sum(array):
        print(0)
    elif isSubsetSum(array, N, K):
        print(1)
    else:
        print(0)
