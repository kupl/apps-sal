T = int(input())


def maxk(arr, start, end):
    maxno = arr[start]
    maxi = start
    for i in range(start, end):
        if arr[i] > maxno:
            maxno = arr[i]
            maxi = i
    return maxi


def rec(arr, start, end):
    i = maxk(arr, start, end)
    if i == start or i == end - 1:
        return 1
    else:
        return 1 + min(rec(arr, i + 1, end), rec(arr, start, i))


for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    start = 0
    end = n
    count = rec(arr, start, end)
    print(count)
