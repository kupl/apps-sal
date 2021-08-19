from collections import defaultdict


def findSubarraySum(arr, n, Sum):

    # Dictionary to store number of subarrays
    # starting from index zero having
    # particular value of sum.
    prevSum = defaultdict(lambda: 0)

    res = 0

    # Sum of elements so far.
    currsum = 0

    for i in range(0, n):

        # Add current element to sum so far.
        currsum += arr[i]

        # If currsum is equal to desired sum,
        # then a new subarray is found. So
        # increase count of subarrays.
        if currsum == Sum:
            res += 1

        # currsum exceeds given sum by currsum  - sum.
        # Find number of subarrays having
        # this sum and exclude those subarrays
        # from currsum by increasing count by
        # same amount.
        if (currsum - Sum) in prevSum:
            res += prevSum[currsum - Sum]

        # Add currsum value to count of
        # different values of sum.
        prevSum[currsum] += 1

    return res


n = int(input())
lst = list(map(int, input().split()))
if(n == 1):
    if(lst[0] == 0):
        print(1)
    else:
        print(0)
else:
    print(findSubarraySum(lst, n, 0))
