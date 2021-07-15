import math
def find_smallest_int(arr):
    # Code here
    min=arr[0]
    for i in range(0,len(arr)):
        if(arr[i]<min):
            min=arr[i]
    return min

