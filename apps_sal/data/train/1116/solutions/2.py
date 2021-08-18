from collections import defaultdict


def findSubarraySum(arr, n, Sum):

    prevSum = defaultdict(lambda: 0)

    res = 0

    currsum = 0

    for i in range(0, n):

        currsum += arr[i]

        if currsum == Sum:
            res += 1

        if (currsum - Sum) in prevSum:
            res += prevSum[currsum - Sum]

        prevSum[currsum] += 1

    return res


n = int(input())
arr = [int(i) for i in input().split()]
Sum = 0
print(findSubarraySum(arr, n, Sum))
