def equable_triangle(a,b,c):
    return a+b+c==((a+(b+c))*(c-(a-b))*(c+(a-b))*(a+(b-c)))**0.5/4
