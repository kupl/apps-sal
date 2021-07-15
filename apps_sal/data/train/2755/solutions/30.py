def multiple_of_index(arr):
    nArr=[]
    for i in range(1,len(arr)):
        if arr[i]%i==0: nArr.append(arr[i])
    return nArr
