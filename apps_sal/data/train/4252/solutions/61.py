def merge_arrays(first, second):
    arr = first + second
    arr1=[]
    for i in arr:
        if i not in arr1:
            arr1.append(i)
    return sorted(arr1)
