def f(a, y, index, sorted_pos):
    n = len(a)
    low = 0
    high = n - 1
    (L, R) = (0, 0)
    (l, r) = (0, 0)
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == y:
            break
        elif mid > index[y]:
            high = mid - 1
            L += 1
            if a[mid] < y:
                l += 1
        else:
            low = mid + 1
            R += 1
            if a[mid] > y:
                r += 1
    x = sorted_pos[y]
    if R > x or L > n - x - 1:
        print('-1')
    else:
        print(max(l, r))


def fun():
    test = int(input())
    for t in range(test):
        (n, q) = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        index = dict()
        for i in range(n):
            index[arr[i]] = i
        sorted_pos = dict()
        a = sorted(arr)
        for i in range(n):
            sorted_pos[a[i]] = i
        for x in range(q):
            y = int(input())
            f(arr, y, index, sorted_pos)


fun()
