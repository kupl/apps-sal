def char_freq(m):
    o={}
    for i in range(0,len(m)):
       if not o.get(m[i]): o[m[i]]=1 
       else: o[m[i]]=o[m[i]]+1
    return o
