def expression_matter(a, b, c):
    return max(a*(c+b), a*b*c, a+b+c, a+b*c, (a+b)*c)
