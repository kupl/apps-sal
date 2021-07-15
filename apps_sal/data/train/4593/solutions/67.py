def merge_arrays(arr1, arr2):
    newarr=arr1+arr2
    ls=[]
    for i in newarr:
        if i in ls:
            continue
        ls.append(i)
    ls.sort()
    return ls
