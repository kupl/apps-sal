def simplify(n):

    for i in range(int(n**.5),1,-1):
        if not n%(i*i):
            s = f'{i} sqrt {n//(i*i)} '
            break
    else:
        s = f' sqrt {n} '

    return s.replace(' sqrt 1 ','').strip() or '1'

def desimplify(s):
    s = s.split()
    if len(s)==3:
        a,b = map(int,(s[0],s[-1]))
        return a*a*b
    if len(s)==1:
        return int(s[-1])**2
    return int(s[-1])
