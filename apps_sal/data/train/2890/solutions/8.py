def multiples(m, n):
    l=[]
    count=1
    while len(l)<m:
        l.append(n*count)
        count+=1
    return l    
        

