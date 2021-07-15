import collections
def duplicates(arr: list):
    sumDup = 0
    arr = collections.Counter(arr)
    for i in arr:
        sumDup += arr[i] // 2
    return sumDup
