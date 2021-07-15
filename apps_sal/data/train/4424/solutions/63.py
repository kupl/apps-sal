def expression_matter(a, b, c):
    lt = [a*(b+c), (a+b)*c, a*b*c, a+b*c, a*b+c, a+b+c]
    return max(lt)
