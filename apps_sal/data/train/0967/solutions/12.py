def isSubsetSum(set, n, sum):
    if sum == 0:
        return 1
    if n == 0 and sum != 0:
        return 0
    if set[n - 1] > sum:
        return isSubsetSum(set, n - 1, sum)
    return isSubsetSum(set, n - 1, sum) + isSubsetSum(set, n - 1, sum - set[n - 1])


def __starting_point():
    t = int(input())
    while t > 0:
        n = int(input())
        m = int(input())
        arr = list(map(int, input().split()))
        print(isSubsetSum(arr, n, m))
        t -= 1


__starting_point()
