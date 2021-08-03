# import os, sys, atexit
# from io import BytesIO, StringIO
from sys import stdin, stdout

# input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
# _OUTPUT_BUFFER = StringIO()
# sys.stdout = _OUTPUT_BUFFER

# @atexit.register
# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def calculate(array):
    n = len(array)
    finalarray = []
    finalarray.append(array)
    finalarray.append([])
    while (n != 1):
        for x in range(n - 1):
            finalarray[-1].append(finalarray[-2][x] ^ finalarray[-2][x + 1])
        finalarray.append([])
        n -= 1
    return finalarray


def solve():
    n = int(input())
    array = [0]
    array.extend(list(map(int, stdin.readline().strip().split())))
    subArrays = []
    for x in range(n + 1):
        subArrays.append([0] * (n + 1))
    finalarray = calculate(array)
    # print (finalarray,len(finalarray))
    for x in range(1, n + 1):
        for y in range(x, n + 1):
            # print (y-x+1,x,finalarray[y-x+1])
            value = finalarray[y - x][x]
            subArrays[1][y] = max(subArrays[1][y], value)
            subArrays[x][y] = max(subArrays[x][y], value)
    # print (subArrays)
    for x in range(1, n + 1):
        for y in range(2, n + 1):
            subArrays[x][y] = max(subArrays[x][y], subArrays[x][y - 1])
    # print (subArrays)
    for y in range(1, n + 1):
        for x in range(n - 1, 0, -1):
            subArrays[x][y] = max(subArrays[x][y], subArrays[x + 1][y])
    # print (subArrays)
    q = int(input())
    for _ in range(q):
        l, r = list(map(int, stdin.readline().strip().split()))
        print(subArrays[l][r])


try:
    solve()
except Exception as e:
    print(e)

# solve()
