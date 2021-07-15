def merge_arrays(arr1, arr2):
    ans=[]
    for x in arr1:
        if x not in ans:
            ans.append(x)
    for x in arr2:
        if x not in ans:
            ans.append(x)
    return sorted(ans)
