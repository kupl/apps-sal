def circularly_sorted(arr):
    temp = sorted(arr)
    for i in range(len(arr)):
        temp = temp[1:]+[temp[0]]    
        if temp==arr : return 1
    return 0
