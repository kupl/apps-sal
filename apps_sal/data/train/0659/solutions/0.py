# binarr
def binarr(a, k, s):
    a.sort(reverse=True)
    arr = [0] * k
    for i in range(k):
        arr[i] = a[i]
    if sum(arr) <= s:
        return binarr(a, k + 1, s)
    return len(arr)


try:
    n, k, s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(binarr(a, k + 1, s))
except Exception:
    pass
