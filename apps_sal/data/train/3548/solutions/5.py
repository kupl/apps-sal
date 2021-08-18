def polynomialize(roots):
    def add_root(poly, root):
        poly1 = poly + [0]
        poly2 = [0] + [-root * coef for coef in poly]
        poly = [coef1 + coef2 for coef1, coef2 in zip(poly1, poly2)]
        return poly

    def poly2str(poly):
        spoly = ""
        for i, coef in enumerate(poly):
            if i == 0:
                signum = ""
            elif coef > 0:
                signum = " + "
            elif coef < 0:
                signum = " - "
            else:
                continue

            if abs(coef) == 1:
                scoef = ""
            else:
                scoef = str(abs(coef))

            exp = len(poly) - i - 1
            if exp == 1:
                sexp = "x"
            elif exp == 0:
                if scoef == "":
                    sexp = "1"
                else:
                    sexp = ""
            else:
                sexp = "x^" + str(exp)
            spoly += signum + scoef + sexp
        spoly += " = 0"
        return spoly

    poly = [1, -roots[0]]
    for root in roots[1:]:
        poly = add_root(poly, root)

    return poly2str(poly)
