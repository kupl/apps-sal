def find_uniq(arr):
    culprit = arr[1]
    if arr[0] == arr[2]:
        culprit = arr[0]
    for i in arr:
        if i != culprit:
            return i
