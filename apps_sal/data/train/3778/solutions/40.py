def find_smallest_int(arr):
    arr.sort()
    arr.reverse()
    return arr.pop()
