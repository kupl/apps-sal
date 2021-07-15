def multiple_of_index(arr):
    return [arr[i] for i in range(0 if arr[0]==0 else 1,len(arr)) if arr[i]%i==0]
