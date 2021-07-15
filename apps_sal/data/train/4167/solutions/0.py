def descriptions(arr):
    return 2**sum(a+1==b for a,b in zip(arr,arr[1:]))
