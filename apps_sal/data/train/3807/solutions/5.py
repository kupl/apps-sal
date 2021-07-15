def smaller(arr):
    return [sum(1 for right in arr[i+1:] if right<item) for i,item in enumerate(arr)]
