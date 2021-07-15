def cube_odd(arr):
    res=0
    for i in arr:
        if isinstance(i,int) and not isinstance(i,bool):
            if (i**3)%2==1:
                res+=i**3
        else:
            return None
    return res
