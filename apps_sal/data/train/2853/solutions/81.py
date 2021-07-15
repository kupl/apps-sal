def solve(arr): 
    b = reversed(arr)
    new =[]
    for i in b:
        if i not in new:
            new.append(i)
    arr=new
    arr.reverse()
    return arr
    pass
