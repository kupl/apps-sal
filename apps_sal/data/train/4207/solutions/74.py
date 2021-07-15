def sum_cubes(n):
    if n==1:
        return 1
    LV=[]
    for i in range(n+1):
        res=i**3
        LV.append(res)
    return sum(LV)
