def search_substr(ft, st, allow_overlap=True):
    if not st: return 0
    i,L,M,r,x = 0,len(ft),len(st),0,1
    if not allow_overlap: x = M
    while i + M <= L:
        if ft[i:i+M] == st: r,i = r+1,i+x-1
        i += 1
    return r
