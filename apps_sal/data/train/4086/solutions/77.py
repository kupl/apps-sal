def first_non_consecutive(arr):
    ans = arr[0]
    for i in arr:
        if ans != i:
            return i
        else:
            ans += 1
    return None

