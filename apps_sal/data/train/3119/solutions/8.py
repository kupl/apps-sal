def pattern(*args):
    n=args[0]
    y=args[1] if len(args)>=2 else 0
    res=""
    for count in range(max(1,y)):
        for i in range(n):
            if count>=1 and (i+1)==1:
                continue
            elif (i+1)!=n:
                res+=" "*i+str((i+1)%10)+" "*((n-1-i)*2-1)+str((i+1)%10)+" "*i+"\n"
            else:
                res+=" "*i+str((i+1)%10)+" "*i+"\n"
        for i in range(n-2,-1,-1):
            if (i+1)!=n:
                res+=" "*i+str((i+1)%10)+" "*((n-1-i)*2-1)+str((i+1)%10)+" "*i+"\n"
    return res[:-1]
