res=[]
for i in range(int(input())):
    n=input()
    x=list(n)
    re=""
    for i in x:
        if i=="'" or i==";" or i=="," or i==":" or i==".":
            continue
        else:
            re+=i
    t=[]
    p=""
    p1=len(re)
    i=0
    while i < p1:
        if re[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            p+=re[i]
            i+=1
        elif re[i]==" ":
            try:
                while re[i]==" ":
                    i+=1
            except:
                break
            t.append(p)
            p=""
    t.append(p)
    t=t[::-1]
    res.append(t)
res=res[::-1]
for i in res:
    print(*i)



