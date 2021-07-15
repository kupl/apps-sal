def hyperrectangularity_properties(arr):
    v = len(arr)
    k = (v,)
    if not v: return k
    if len( set(map(type, arr)) )!= 1: return None
    if isinstance(arr[0], int): return k
    rest = list(  set(map(hyperrectangularity_properties, arr)) )
    if len(rest) == 1 and rest[0] != None:
        return k + rest[0]
    return None

