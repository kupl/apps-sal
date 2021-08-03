def expression_matter(a, b, c):
    var1 = a * (b + c)
    var2 = a * b * c
    var3 = a + b * c
    var4 = (a + b) * c
    var5 = a + b + c
    sum = []
    sum.append(var1)
    sum.append(var2)
    sum.append(var3)
    sum.append(var4)
    sum.append(var5)

    sum = sorted(sum)
    return sum[-1]
