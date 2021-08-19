def solve(arr):
    (holder, result) = ({}, [])
    index = len(arr) - 1
    while 0 <= index:
        if arr[index] not in holder:
            result.insert(0, arr[index])
            holder[arr[index]] = True
        index -= 1
    return result
