def find_longest(arr):
    newArray = list(map(str, arr))
    return int(max(newArray, key=len))
