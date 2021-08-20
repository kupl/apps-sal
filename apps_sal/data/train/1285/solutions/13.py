import numpy as np
'\ndef findTrace(i,j,k):\n    trace = 0\n    for z in range(0,k+1):\n     trace+=matrix[i+z][j+z]\n    return trace\n'


def traceSum(matrix, n):
    (sum, round, j) = (0, n - 1, 0)
    i = round
    sumArray = []
    while i >= 0:
        while i < n:
            sum += matrix[i][j]
            i += 1
            j += 1
        round -= 1
        (i, j) = (round, 0)
        sumArray.append(sum)
        sum = 0
    round = n - 1
    (i, j) = (0, round)
    while j > 0:
        while j < n:
            sum += matrix[i][j]
            i += 1
            j += 1
        round -= 1
        (i, j) = (0, round)
        sumArray.append(sum)
        sum = 0
    return max(sumArray)


t = int(input())
for i in range(t):
    n = int(input())
    a = []
    for i in range(0, n):
        ele = list(map(int, input().split()))
        a.append(ele)
    matrix = np.array(a).reshape(n, n)
    '\n    This worked but had a n^3 complexity and gave an error of time limit \xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0exceeded on submission.\n    trace = 0\n    for i in range(0,n):   #Row number\n     for j in  range(0,n):   #Column number\n      for k in range(0,n):   #Length of Sub-matrix\n       if i+k<n and j+k<n:\n        trace = max(trace,findTrace(i,j,k))  #Check trace of every \xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0sub-matrix & get max\n        '
    print(traceSum(matrix, n))
