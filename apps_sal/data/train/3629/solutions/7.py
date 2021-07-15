def array_mash(a, b):
    for v,y in zip (range(1,len(b)*2,2),b):
        a.insert(v, y) 
    return a
