# return the sum of the two polynomials p1 and p2.
def poly_add(p1, p2):
    if p1 == []:
        return p2
    if p2 == []:
        return p1
    return [p1[0] + p2[0]] + poly_add(p1[1:], p2[1:])
