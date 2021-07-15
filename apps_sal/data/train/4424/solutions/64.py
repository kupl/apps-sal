def expression_matter(a, b, c):
    all = [a+b+c, a+b*c, a*b+c, a*b*c, (a+b)*c, a*(b+c)]
    return max(all)
        

