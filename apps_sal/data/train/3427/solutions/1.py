def find_uniq(arr):
    if arr[0] == arr[1]:
        return [x for x in arr[2:] if x != arr[0]][0]
    return arr[0] if arr[1] == arr[2] else arr[1]
