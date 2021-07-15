def slogan_maker(array):
    ls=[]
    for i in array:
        if i not in ls:
            ls.append(i)
    if len(ls) ==0:
        return []
    if len(ls) ==1:
        return ls
    l=[]
    for i in range(len(ls)):
        e = ls[i]
        re = [i for i in ls if i!=e]
        
        for p in slogan_maker(re):
            l.append(e+" "+p)
    return l
