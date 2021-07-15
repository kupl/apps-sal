a=[3];b=[1];c=[2];d=[1];e=[2];f=[3];g=[1];h=[1];i=[1];j=[8]

for _ in range(10000):
    next_a = 3*a[-1] + b[-1] + e[-1] + f[-1] + h[-1] + i[-1] + 3*j[-1]
    next_b = a[-1] + 2*b[-1] + e[-1] + i[-1] + j[-1]
    next_c = 2*c[-1] + d[-1] + f[-1] + g[-1] + 2*j[-1]
    next_d = c[-1] + 2*d[-1] + f[-1] + g[-1] + j[-1]
    next_e = a[-1] + b[-1] + 2*e[-1] + i[-1] + 2*j[-1]
    next_f = a[-1] + c[-1] + d[-1] + 3*f[-1] + g[-1] + h[-1] + 3*j[-1]
    next_g = c[-1] + d[-1] + f[-1] + g[-1] + j[-1]
    next_h = a[-1] + f[-1] + h[-1] + j[-1]
    next_i = a[-1] + b[-1] + e[-1] + i[-1] + j[-1]
    next_j = 3*a[-1] + b[-1] + 2*c[-1] + d[-1] + 2*e[-1] + 3*f[-1] + g[-1] + h[-1] + i[-1] + 8*j[-1]
    a.append(next_a%12345787)
    b.append(next_b%12345787)
    c.append(next_c%12345787)
    d.append(next_d%12345787)
    e.append(next_e%12345787)
    f.append(next_f%12345787)
    g.append(next_g%12345787)
    h.append(next_h%12345787)
    i.append(next_i%12345787)
    j.append(next_j%12345787)
    
def five_by_2n(n):
    return j[n-1]
