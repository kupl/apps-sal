def isSubsetSum(arr, n, sum):
    subset = [[False for j in range(sum + 1)] for i in range(3)]
    for i in range(n + 1):
        for j in range(sum + 1):
            if (j == 0):
                subset[i % 2][j] = True
            elif (i == 0):
                subset[i % 2][j] = False
            elif (arr[i - 1] <= j):
                subset[i % 2][j] = subset[(i + 1) % 2][j - arr[i - 1]] or subset[(i + 1) % 2][j]
            else:
                subset[i % 2][j] = subset[(i + 1) % 2][j]
    return subset[n % 2][sum]


for _ in range(int(input())):
    k, n, a = int(input()), int(input()), list(map(int, input().split()))
    if sum(a) < k or k < min(a):
        print(0)
        continue
    print(1) if isSubsetSum(a, n, k) else print(0)
