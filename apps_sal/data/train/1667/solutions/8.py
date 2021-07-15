def unflatten(flat_array, depth):
    bLeft=True
    for i in range(depth):
        flat_array=oneunflatten(flat_array,bLeft)
        if bLeft==False:
            flat_array=flat_array[::-1]
        bLeft = not bLeft
    return flat_array
    
def oneunflatten(flat_array, bLeft):
    if bLeft:
        arr = flat_array[:]
        for i, v in enumerate(arr):
            if isinstance(v,int):
                if v%(len(arr)-i) > 2:
                    arr[i], arr[i+1:i+v%(len(arr)-i)] = arr[i:i+v%(len(arr)-i)], []
            else:
                arr[i]=oneunflatten(v,bLeft)
        return arr
    else:
        arr = flat_array[::-1]
        for i, v in enumerate(arr):
            if isinstance(v,int):
                if v%(len(arr)-i) > 2:
                    arr[i], arr[i+1:i+v%(len(arr)-i)] = arr[i:i+v%(len(arr)-i)], []
            else:
                arr[i]=oneunflatten(v,bLeft)
        for i, v in enumerate(arr):
            if isinstance(v,int):
                pass
            else:
                arr[i]=arr[i][::-1]
        return arr
