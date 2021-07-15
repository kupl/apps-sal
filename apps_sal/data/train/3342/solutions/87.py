def pattern(n):
    s=''
    if n<1:
        return s
    else:
        for i in range(1,n+1):
            s+=str(i)*i+'\n'
    return s.rstrip()

