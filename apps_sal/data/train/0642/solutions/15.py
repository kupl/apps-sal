def binary_search(arr, x):
    arr.sort()
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:

        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def ternary_search(l, r, key, ar):
    if (r >= l):
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if (ar[mid1] == key):
            return mid1
        if (ar[mid2] == key):
            return mid2
        if (key < ar[mid1]):
            return ternary_search(l, mid1 - 1, key, ar)
        elif (key > ar[mid2]):
            return ternary_search(mid2 + 1, r, key, ar)
        else:
            return ternary_search(mid1 + 1,
                                  mid2 - 1, key, ar)
    return -1


def cheaker(c, d, val, n):
    st = c[0]
    for i in range(1, n):
        if st + val < c[i]:
            st = c[i]
        elif st + val > c[i] + d:
            return False
        else:
            st += val
    return True


def binary_search_answer(low, high, d, a, n, de):
    x = 1
    p = 0
    while(p != d):
        while((high - low) > x):
            mid = (high + low) / 2
            if cheaker(a, de, mid, n):
                low = mid
            else:
                high = mid
        x /= 10
        p += 1
    return low


def __starting_point():
    for i in range(int(input())):
        n, d = list(map(int, input().split()))
        a = [int(X) for X in input().split()]
        a.sort()
        print(round(binary_search_answer(0, 2 * (10**9), 7, a, n, d), 10))


__starting_point()
