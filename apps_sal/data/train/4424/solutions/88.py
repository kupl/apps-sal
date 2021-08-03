def expression_matter(a, b, c):
    rez1 = a * (b + c)
    rez2 = a * b * c
    rez3 = a + b * c
    rez4 = (a + b) * c
    rez5 = a + b + c
    return max(rez1, rez2, rez3, rez4, rez5)
