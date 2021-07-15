def find_longest(arr):
    biggest = arr[0]
    for num in arr:
        if len(str(num)) > len(str(biggest)):
            biggest=num
    return biggest
