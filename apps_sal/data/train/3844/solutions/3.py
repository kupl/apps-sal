def poly_from_roots(r):
    lst = [1]
    while r:
        v   = -r.pop()
        lst.append(0)
        lst = [1 if i==len(lst)-1 else x*v+lst[i-1] for i,x in enumerate(lst)]
    return lst

