def explode(arr):
    l=sum(type(v)==int for v in arr)
    if not l:return'Void!'
    return[arr]*sum(v for v in arr if type(v)==int)
