def merge_arrays(arr1, arr2):
    ans=arr1+arr2
    ans= list(set(ans))
    ans.sort()
    return ans

