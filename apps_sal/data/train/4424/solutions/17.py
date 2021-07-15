def expression_matter(a, b, c):
    m1 = a*(b+c)
    m2 = a*b*c
    m3 = a+b*c
    m4 = (a+b)*c
    m5 = a+b+c
    large = m1
    if m2 > large:
        large = m2
    if m3 > large:
        large = m3
    if m4 > large:
        large = m4
    if m5 > large:
        large = m5
    return large
