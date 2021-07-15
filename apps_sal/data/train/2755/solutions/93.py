def multiple_of_index(arr):
    array=[]
    for x in range(1,len(arr),1):
        if arr[x] % x ==0:
            array.append(arr[x])
    return array
