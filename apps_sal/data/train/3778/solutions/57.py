def find_smallest_int(arr):
    small = 100000000000000000000
    for i in arr:
        while(i < small):
            small = i
    return small
