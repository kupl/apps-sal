def cube_odd(arr):
    s = 0
    for i in arr:
        if type(i) == bool or type(i) == str:
            return None
        else:
            if i%2==1:
                s += i**3
    return s
