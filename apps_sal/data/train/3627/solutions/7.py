def sort_two_arrays(arr1, arr2):
    k1=sorted((v,i)for i,v in enumerate(arr1))
    k2=sorted((v,i)for i,v in enumerate(arr2))
    return[[arr1[i]for v,i in k2],[arr2[i]for v,i in k1]]
