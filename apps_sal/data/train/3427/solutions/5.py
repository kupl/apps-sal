def find_uniq(arr):
    if arr[0] != arr[1]:
        if arr[0] != arr[2]:
            return arr[0]
        else:
            return arr[1]
    else:
        for i in arr[2:]:
            if i != arr[0]:
                return i
