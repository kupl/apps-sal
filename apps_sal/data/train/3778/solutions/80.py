def find_smallest_int(arr):
    smallest = None
    for number in arr:
        if smallest is None: 
            smallest = number
        elif number < smallest:
            smallest = number
        else: 
            continue
    return smallest
