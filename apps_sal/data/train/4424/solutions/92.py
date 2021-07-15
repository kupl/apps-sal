def expression_matter(a, b, c):
    res = max(a*(b+c),a*b*c,a+b*c,(a+b)*c,a+b+c)
    return res

a = 2
b = 1
c = 2
print(expression_matter(a,b,c))
