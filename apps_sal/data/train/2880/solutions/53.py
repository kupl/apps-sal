def seven(m):
    s=0
    while m>99:
        a,b=divmod(m,10)
        m=a-2*b
        s+=1
    return m,s
