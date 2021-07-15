def solve(n):
    lst = list(range(2,n+1))
    res = [1]
    
    while lst and len(lst) > lst[0]:
        idx = lst[0]
        lst = [x for i,x in enumerate(lst) if i % idx]
        res.append(idx)
        
    return sum(res) + sum(lst)
