def polynomialize(roots):
    poly = [1]
    for root in roots:
        new_poly = [1]
        for i in range(1, len(poly)):
            new_poly.append(poly[i] - root * poly[i - 1])
        new_poly.append(poly[-1] * -root)
        poly = new_poly
    
    str_poly = []
    for i, coeff in enumerate(poly):
        power = len(roots) - i
        if coeff < 0:
            str_poly.append(' - ')
        elif coeff > 0:
            if i:
                str_poly.append(' + ')
        else:
            continue
        coeff = abs(coeff)
        if power == 0 or coeff != 1:
            str_poly.append(str(coeff))
        if power != 0:
            str_poly.append('x')
        if power >= 2:
            str_poly.append('^')
            str_poly.append(str(power))
    return f'{"".join(str_poly)} = 0'
