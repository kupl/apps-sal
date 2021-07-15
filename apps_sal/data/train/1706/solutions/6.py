def rectangle_rotation(a, b):
    n1, n2 = map(lambda x: int((x/2) / 2**.5), [a,b])
    m1, m2 = map(lambda x: int((x-2**.5)/2 / 2**.5 + 1), [a,b])
    return (2*n1+1)*(2*n2+1) + 4*m1*m2
