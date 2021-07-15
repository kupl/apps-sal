def minimum(arr):
    #first we define the Minimum value 'Min' to be the first value in the array for comparison
    Min=arr[0]
    #Next we loop through the array to check if each value is smaller than the first. If it is, make that the new Min value
    for i in arr:
        if i<Min:
            Min=i
    return Min

def maximum(arr):
    #first we define the Maximum value 'Max' to be the first value in the array for comparison
    Max=arr[0]
    #Next we loop through the array to check if each value is bigger than the first. If it is, make that the new Max value
    for i in arr:
        if i>Max:
            Max=i
    return Max
