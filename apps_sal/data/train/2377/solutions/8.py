from sys import stdin


def bsearch(lis, idx, val):
    l = 0
    h = idx
    while(l <= h):
        mid = (l + h) // 2
        if lis[mid] == val:
            return mid
        if lis[mid] > val:
            h = mid - 1
        else:
            l = mid + 1


def res(arr):
    lis_f = sorted(arr)
    _arr = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        _arr[bsearch(lis_f, len(arr) - 1, arr[i])] = i
    c = 1
    p = 0
    for j in range(1, len(arr)):
        if _arr[j] > _arr[j - 1]:
            c += 1
        elif c > p:
            p = c
            c = 1
        else:
            c = 1
    if c > p:
        p = c
    print(len(arr) - p)


k = int(stdin.readline())
while(k):
    stdin.readline()
    res(list(map(int, stdin.readline().split())))
    k -= 1
