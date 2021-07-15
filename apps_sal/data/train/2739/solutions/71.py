def cube_odd(arr):
    res=[]
    for i in arr:
        if not type(i)==int :
           return None
        if i%2:
           res.append(i**3)
    return sum(res)

