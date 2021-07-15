def solve(arr):
    res=[]
    for i in arr:
        c=0
        for j in range(len(i)):
            if j==ord(i.upper()[j])-65:
               c+=1
        res+=[c]
    return res

