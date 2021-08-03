# dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]


def kadane(arr, start, finish, n):
    Sum = 0
    maxSum = float('-inf')
    i = None
    finish[0] = -1
    local_start = 0
    for i in range(n):
        Sum += arr[i]
        if Sum < 0:
            Sum = 0
            local_start = i + 1
        elif Sum > maxSum:
            maxSum = Sum
            start[0] = local_start
            finish[0] = i

    if finish[0] != -1:
        return maxSum

    maxSum = arr[0]
    start[0] = finish[0] = 0

    for i in range(1, n):
        if arr[i] > maxSum:
            maxSum = arr[i]
            start[0] = finish[0] = i
    return maxSum


def findMaxSum(M):
    nonlocal ROW, COL
    maxSum, finalLeft = float('-inf'), None
    finalRight, finalTop, finalBottom = None, None, None
    left, right, i = None, None, None

    temp = [None] * ROW
    Sum = 0
    start = [0]
    finish = [0]

    for left in range(COL):
        temp = [0] * ROW
        for right in range(left, COL):
            for i in range(ROW):
                temp[i] += M[i][right]
            Sum = kadane(temp, start, finish, ROW)
            if Sum > maxSum:
                maxSum = Sum
                finalLeft = left
                finalRight = right
                finalTop = start[0]
                finalBottom = finish[0]

    for i in range(finalTop, finalBottom + 1):
        print(*M[i][finalLeft:finalRight + 1])


ROW, COL = ip()
M = [ip() for i in range(ROW)]
findMaxSum(M)
