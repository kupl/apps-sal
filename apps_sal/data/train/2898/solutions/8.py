def find_array(arr1, arr2):
    return [] if len(arr1)*len(arr2)==0 else [arr1[i] for i in arr2 if i<len(arr1)]
