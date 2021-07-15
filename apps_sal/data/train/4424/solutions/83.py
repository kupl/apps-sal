def expression_matter(a, b, c):
    abc1 = a * (b+c)
    abc2 = a*b*c
    abc3 = a+b*c
    abc4 = (a+b) * c
    abc5 = a + b +c
    return max(abc1,abc2,abc3,abc4, abc5)

