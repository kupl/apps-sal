def minimum(arr):
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped=True
    return arr[0]

def maximum(arr):
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped=True
    return max(arr)
    #...and here

