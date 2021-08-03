import numpy as np
'''
def findTrace(i,j,k):
    trace = 0
    for z in range(0,k+1):
     trace+=matrix[i+z][j+z]
    return trace
'''


def traceSum(matrix, n):
    sum, round, j = 0, n - 1, 0
    i = round
    sumArray = []

    while (i >= 0):
        while(i < n):
            sum += matrix[i][j]
            i += 1
            j += 1

        round -= 1
        i, j = round, 0
        sumArray.append(sum)
        sum = 0

    round = n - 1
    i, j = 0, round

    while (j > 0):
        while(j < n):
            sum += matrix[i][j]
            i += 1
            j += 1

        round -= 1
        i, j = 0, round
        sumArray.append(sum)
        sum = 0
    return max(sumArray)


t = int(input())
for i in range(t):
    # Array Size is n
    n = int(input())
    a = []

    for i in range(0, n):
        ele = list(map(int, input().split()))
        a.append(ele)

    matrix = np.array(a).reshape(n, n)

    # print(matrix)
    '''
    This worked but had a n^3 complexity and gave an error of time limit         exceeded on submission.
    trace = 0
    for i in range(0,n):   #Row number
     for j in  range(0,n):   #Column number
      for k in range(0,n):   #Length of Sub-matrix
       if i+k<n and j+k<n:
        trace = max(trace,findTrace(i,j,k))  #Check trace of every                         sub-matrix & get max
        '''
    print(traceSum(matrix, n))
