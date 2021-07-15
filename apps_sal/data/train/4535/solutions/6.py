def zfunc(str_):
    if not str_:
        return []
    r=[len(str_)]
    for i in range(1,len(str_)):
        j=0
        l=len(str_)-i
        if str_[:l]==str_[i:]:
            r.append(l)
            continue
        while(i+j<len(str_) and str_[j]==str_[i+j]):
            j+=1
        r.append(j)
    return r
