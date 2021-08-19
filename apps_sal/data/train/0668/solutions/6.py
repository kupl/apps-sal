import sys


def maxSubArraySum(a, n, k):
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0
    for i in range(n * k):
        max_ending_here = max_ending_here + a[i % n]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


for _ in range(int(input())):
    (n, k) = map(int, input().split())
    ar = [int(x) for x in input().split()]
    s = sum(ar)
    if s >= 0:
        if k == 1 or k == 2:
            print(maxSubArraySum(ar, n, k))
        else:
            print(maxSubArraySum(ar, n, 2) + (k - 2) * s)
    elif k == 1:
        print(maxSubArraySum(ar, n, k))
    else:
        print(maxSubArraySum(ar, n, 2))
