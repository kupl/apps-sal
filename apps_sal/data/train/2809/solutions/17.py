def digitize(n):
    n=str(n)
    arr=[]
    for u in n:
        arr.append(int(u))
    arr=arr[::-1]
    return arr
