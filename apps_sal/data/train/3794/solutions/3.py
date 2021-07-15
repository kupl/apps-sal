def nth_smallest(arr,k):
   
    if len(set(arr)) == 1:
        return arr[0]
    else:
        if len(set(arr)) < k:
            return None

    pivot = arr[0]
    lesser = list(set([x for x in arr[1:] if x < pivot]))
    greater = list(set([x for x in arr[1:] if x > pivot]))

    if len(lesser) >= k:
        return nth_smallest(lesser,k)
    
    elif len(lesser) == k-1:
        return pivot
    
    else:
        return nth_smallest(greater, k-len(lesser)-1)

