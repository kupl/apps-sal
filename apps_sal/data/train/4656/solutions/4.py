def center_of(chars):
    if not chars:
        return ""
    total=0
    res=[]
    for i in range(1,len(chars)*2+1):       
        if i%2==1:
            res.append((i+1)//2+total)
            res[(i-1)//2]=chars[(res[(i-1)//2]-1)%len(chars)]
        total+=i
    check="".join(res)
    for i in range(len(check)//2+1):
        if len(check)%len(check[:i+1])!=0:
            continue
        if check[:i+1]*(len(check)//len(check[:i+1]))==check:
            return check[:i+1]
    return check
