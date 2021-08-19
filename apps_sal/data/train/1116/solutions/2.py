# # we could probably do N linear searches or something
# # time limit is 2 seconds which makes sense for O(n^2) or something
# N = int(input());count = 0
# arr = list(map(int , input().split()))
# for i in range(N):
#     sum_ = arr[i]
#     if(sum_ == 0): count += 1
#     for j in range(i + 1,N):
#         sum_ += arr[j]
#         if(sum_ == 0): count += 1
# print(count) #TLE
# Python3 program to find the number of
# subarrays with sum exactly equal to k.
from collections import defaultdict

# Function to find number of subarrays
# with sum exactly equal to k.


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

        # currsum exceeds given sum by currsum - sum.
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
arr = [int(i) for i in input().split()]
Sum = 0
print(findSubarraySum(arr, n, Sum))

# This code is contributed by Rituraj Jain
