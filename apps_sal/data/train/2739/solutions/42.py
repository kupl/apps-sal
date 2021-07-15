def cube_odd(arr):
    #your code here - return None if at least a value is not an integer
    s = 0
    for i in arr:
        if type(i)!=int:
            return None
        elif i%2==1:
            s+=i**3
        else:
            continue
    return s
