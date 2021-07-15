def merge_arrays(arr1, arr2):
    arr1.sort()
    arr2.sort()
    arr=arr1+arr2
    u=[]
    for a in arr:
        if a not in u:
            u.append(a)
    u.sort()
    return u
