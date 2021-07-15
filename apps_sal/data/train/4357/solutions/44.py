def nth_smallest(arr, pos):
    arr.sort()
    min = 0
    for i in range(len(arr)):
        pos -= 1
        if(pos == 0):
            min = arr[i]
            break;
    return min
