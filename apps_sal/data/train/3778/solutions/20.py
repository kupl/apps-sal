def find_smallest_int(arr):
    lowest = 10000
    for number in arr:
        if number < lowest:
            lowest = number
    return lowest
