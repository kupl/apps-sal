def sum_arrays(array1,array2):
    if array1 and not array2:
        return array1
    elif not array1 and array2:
        return array2
    if array1 or array2:
        a=''.join(map(str,array1))if array1 else '0'
        b=''.join(map(str,array2)) if array2 else '0'
        c=str(int(a)+int(b))
        c=[-int(v) if i==0 else int(v) for i,v in enumerate(c[1:])] if '-' in c else c
        return list(map(int,c)) if list(map(int,c))!=[0] else []
    
    return []
