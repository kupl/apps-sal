from itertools import zip_longest 
def solve(s):
    print(s)
    a=list( map(s.lower().count, "aeiou"))
    print('lv',sum(a))
    l=len(s)
    lv=sum(a)
    lc=l-lv
    print('l',l,'lc',lc)
    vw,cn=[],[]
    if abs(lv-lc)>1:
        return 'failed'
    elif lv<lc:
        for x in s:
            if x in 'aeiou':
                vw.append(x)
            else:    
                cn.append(x)
        cn=sorted(cn)
        vw=sorted(vw)
        b=list(zip_longest(cn,vw))
    elif lc<=lv:
        for x in s:
            if x in 'aeiou':
                vw.append(x)
            else:    
                cn.append(x)
        cn=sorted(cn)
        vw=sorted(vw)
        b=list(zip_longest(vw,cn))    
    print(vw)           
    print(cn)
     
    lst=[]
    for x in b:
        lst.append(x[0])
        lst.append(x[1])
    print(lst) 
    if lst[-1]==None:
        del lst[-1]
    print(lst)     
    return(''.join(lst))    
