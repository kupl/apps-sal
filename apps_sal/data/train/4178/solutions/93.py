def min_sum(arr):
    arr.sort()
    i=0
    s=0
    while i<len(arr)//2:
        s+=arr[i]*arr[len(arr)-1-i]
        i+=1
    return s
