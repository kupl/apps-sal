def expression_matter(a, b, c):
    x=(a+b)*c
    w=a+b+c
    y=a*(b+c)
    z=a*b*c
    return max(x,w,y,z)
