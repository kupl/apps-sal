def find_smallest_int(arr):
    smallest = arr[0]
    for element in range(len(arr)):
        if arr[element] < smallest:
            smallest = arr[element]
    return smallest        

