def find_smallest_int(arr):
    num = arr[0]
    for i in arr:
        if i < num:
            num = i
        else:
            num = num
    return num

