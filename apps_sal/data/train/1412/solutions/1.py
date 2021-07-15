for _ in range(int(input())):
    d={}
    for __ in range(int(input())):
        c,p=map(str,input().split())
        d[c]=p
    s=input()
    k=""
    for i in range(0,len(s)):
        if(s[i] in d.keys()):
            k=k+d[s[i]]
        else:
            k=k+s[i]
     
    if '.' in k:
        k = k.strip('0').rstrip('.') 
    else:
        k = k.lstrip('0') 
    print(k or '0')

