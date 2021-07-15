def or_arrays(arr1, arr2,n=0):
    res=[]
    i=0
    while i<len(arr1) and i<len(arr2):
        res.append(arr1[i] | arr2[i])
        i+=1
    while i<len(arr1):
        res.append(arr1[i] | n)
        i+=1
    while i<len(arr2):
        res.append(arr2[i] | n)
        i+=1
    return res
