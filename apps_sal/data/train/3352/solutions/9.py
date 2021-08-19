def find_longest(arr):
    # your code here
    newArray = list(map(str, arr))
    return int(max(newArray, key=len))
