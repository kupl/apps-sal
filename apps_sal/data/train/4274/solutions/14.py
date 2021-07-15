def do_math(s) :
    s=s.split()
    for i in s:
        a=sorted(s,key=lambda s:([i for i in s if i.isalpha()]))
    n=[]
    for j in a:
        b=''
        for k in j:
            if k.isdigit():
                b+=k
        n.append(b)
    c=int(n[0])
    for l in range(1,len(n)):
        if l%4==1: c+=int(n[l])
        if l%4==2: c-=int(n[l])
        if l%4==3: c*=int(n[l])
        if l%4==0: c/=int(n[l])
    return round(c)
