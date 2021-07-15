def sum_arrays(arrays,shift):
    arrays_new=[arr[:] for arr in arrays]
    if shift==0:return list(map(sum,zip(*arrays_new)))
    out=[]
    i,j=1,1
    while any(arr for arr in arrays_new):
        out.append(sum(arr.pop(0) for arr in arrays_new[:i] if arr))
        if j%shift==0:i+=1
        j+=1
    return out
