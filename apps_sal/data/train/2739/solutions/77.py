def cube_odd(arr):
    result = 0
    for i in arr:        
        if not isinstance(i, int) or isinstance(i, bool):
            return None
        result += i**3 if i & 1 else 0
    return result
