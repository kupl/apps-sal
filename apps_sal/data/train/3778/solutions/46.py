def find_smallest_int(arr):
    lowest = 10000000000000
    for integer in arr:
        if integer < lowest:
            lowest = integer
    return lowest
