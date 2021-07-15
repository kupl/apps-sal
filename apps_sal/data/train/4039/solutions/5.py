def trans_base(n,b):
    r=''
    while(n>0):
        d=n%b
        r+=str(d) if d<10 else 'x'
        n//=b
    return r[::-1]

def fouriest(i):
    m=[0,None,None]
    for b in range(2,300):
        s=trans_base(i,b)
        if len(s)<m[0]:
            break
        c=s.count('4')
        if c>m[0]:
            m=[c,s,b]
    return '{} is the fouriest ({}) in base {}'.format(i,m[1],m[2])
