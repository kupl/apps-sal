def is_centered(arr,n):
    l = int(len(arr)/2) if len(arr)%2==0 else int((len(arr)-1)/2)
    return any(sum(arr[i:-i])==n for i in range(1, l+1)) or sum(arr)==n
