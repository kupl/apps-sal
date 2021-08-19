def find(arr, n):
    return findl(arr, n, len(arr))


def findl(arr, n, l):
    return sum((findl(arr[1:], n - arr[0] * i, l - i) for i in range(l + 1))) if arr and l > 0 else n == 0 and l >= 0
