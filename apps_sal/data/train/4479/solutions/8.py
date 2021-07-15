def elements_sum(arr, *d):
    d = d[0] if d else 0
    c = []
    for k,v in enumerate(arr):
        try:
            c.append(arr[k][len(arr)-k-1])
        except:
            c.append(d)
    return sum(c)
    
    

