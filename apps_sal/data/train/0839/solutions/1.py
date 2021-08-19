def isSubsetSum(arr, n, sum):

    # The value of subset[i%2][j] will be true
    # if there exists a subset of sum j in
    # arr[0, 1, ...., i-1]
    subset = [[False for j in range(sum + 1)] for i in range(3)]

    for i in range(n + 1):
        for j in range(sum + 1):
            # A subset with sum 0 is always possible
            if (j == 0):
                subset[i % 2][j] = True

            # If there exists no element no sum
            # is possible
            elif (i == 0):
                subset[i % 2][j] = False
            elif (arr[i - 1] <= j):
                subset[i % 2][j] = subset[(i + 1) % 2][j - arr[i - 1]] or subset[(i + 1)
                                                                                 % 2][j]
            else:
                subset[i % 2][j] = subset[(i + 1) % 2][j]

    return subset[n % 2][sum]


# Driver program to test above function
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) < k or k < min(a):
        print(0)
        continue
    if (isSubsetSum(a, n, k) == True):
        print(1)
    else:
        print(0)
