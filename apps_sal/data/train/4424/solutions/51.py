def expression_matter(a, b, c):
    
    
    h = a*b+c
    d = a*(b+c)
    e = a+b*c
    f = (a+b)*c
    g = a*b*c
    i = a+b+c
    list = [h,d,e,f,g,i]
    return max(list)
