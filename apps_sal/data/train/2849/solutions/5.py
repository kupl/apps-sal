def peak(arr):
    l=[i for i in range(len(arr)-1) if sum(arr[:i])==sum(arr[i+1:])]
    return l[0] if l else -1
