def expression_matter(a, b, c):
    var1 = a * (b+c)
    var2 = a * b * c
    var3 = a + b * c
    var4 = (a+b) * c 
    var5 = a + b+ c
    result = sorted([var1,var2,var3,var4,var5])[-1]
    return result 
