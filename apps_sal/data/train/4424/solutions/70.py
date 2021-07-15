def expression_matter(a, b, c):
    l = [a+b+c, a+b*c, a*b+c, a*b*c, (a+b)*c, a+(b*c), a*(b+c)]
    return max(l)
