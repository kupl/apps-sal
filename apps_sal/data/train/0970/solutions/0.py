def posSearch(arr, num):
    l = 0
    r = len(arr)
    if num < arr[l]:
        return 0
    elif num > arr[r - 1]:
        return r
    while l < r:
        m = (l + r) // 2
        if arr[m] == num:
            return -1
        if arr[m] < num < arr[m + 1]:
            return m + 1
        if arr[m] > num:
            r = m
        elif arr[m] < num:
            l = m + 1


for _ in range(int(input())):
    n = int(input())
    narr = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        (x, y) = list(map(int, input().split()))
        a = x + y
        j = posSearch(narr, a)
        print(j)
