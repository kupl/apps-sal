descriptions=lambda arr:2**sum(arr[i]+1==arr[i+1] for i in range(len(arr)-1))
