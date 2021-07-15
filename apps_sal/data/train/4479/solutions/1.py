def elements_sum(arr, d=0):
    a=len(arr)    
    res=0
    for i in arr:
        if len(i)>=a:
            res+=i[a-1]
        else:
            res+=d
        a-=1
    return res
