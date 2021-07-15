def expression_matter(a, b, c):
    l=[]
    o=a*(b+c)
    l.append(o)
    t=a*b*c
    l.append(t)
    th=a+b+c
    l.append(th)
    f=(a+b)*c
    l.append(f)
    return max(l)
