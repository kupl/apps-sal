def solve(n):
    zoznam   =  [int(i) for i in range (2,n+1)]
    res=[1]
    while zoznam != []:
        res.append(zoznam[0])
        del zoznam[0::zoznam[0]]    
    return sum(res)
