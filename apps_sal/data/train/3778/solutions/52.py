def find_smallest_int(arr):
    smallest_num = arr[0]
    for num in range(len(arr)):
        if arr[num] < smallest_num: smallest_num = arr[num]
    return smallest_num
