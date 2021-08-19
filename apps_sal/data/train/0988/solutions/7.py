from math import log2


def findX(arr, n):
    itr = arr[0]
    for i in range(len(arr)):
        if arr[i] > itr:
            itr = arr[i]
    p = int(log2(itr)) + 1
    X = 0
    for i in range(p):
        count = 0
        for j in range(n):
            if arr[j] & 1 << i:
                count += 1
        if count > int(n / 2):
            X += 1 << i
    sum = 0
    for i in range(n):
        sum += X ^ arr[i]
    print(sum)


try:
    t = int(input())
    for _ in range(t):
        ss = int(input())
        arr = list(map(int, input().split()))
        n = len(arr)
        findX(arr, n)
except:
    pass
