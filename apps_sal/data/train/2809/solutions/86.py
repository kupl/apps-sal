def digitize(n):
    n=str(n)
    l=[]
    for elem in n:
        l.append(int(elem))  
    l.reverse()
    return l
