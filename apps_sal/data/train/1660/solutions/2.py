def parse_terms(string):
    poly, add = [], ""
    for i in string:
        if i == "+" and len(add) != 0:
            poly.append(add)
            add = ""
        elif i == "-" and len(add) != 0:
            poly.append(add)
            add = "-"
        else:
            add = add + i
    poly.append(add)
    return poly


def parse_coef(term):
    numbers = "1234567890"
    coef, end = "", 0

    if term == "+":
        return False, 0, term
    else:
        for i in range(len(term)):
            if term[i] in numbers + "-":
                coef = coef + term[i]
            else:
                end = i
                break

    if coef == "":
        return True, 1, term
    elif coef == "-":
        return True, -1, term[1:]
    else:
        return True, int(coef), term[end:]


def simplify(poly):
    print(poly)
    if poly[0] == "+":
        poly = poly.replace("+", "", 1)
        print(poly)

    coeff = []
    poly = parse_terms(poly)
    print(poly)

    for i in range(len(poly)):
        if_term, coef, term = parse_coef(poly[i])
        if if_term:
            coeff.append(coef)
            poly[i] = "".join(sorted(term))

    for i in range(len(poly) - 1):
        for j in range(i + 1, len(poly)):
            if poly[i] == poly[j] and coeff[i] != 0:
                coeff[i] = coeff[i] + coeff[j]
                coeff[j] = 0

    poly = [[poly[i], coeff[i], len(poly[i])] for i in range(len(poly))]
    poly.sort(key=lambda poly: poly[0])
    poly.sort(key=lambda poly: poly[2])
    print(poly)

    for i in range(len(poly)):
        if poly[i][1] == 1:
            pass
        elif poly[i][1] == -1:
            poly[i][0] = "-" + poly[i][0]
        elif poly[i][1] == 0:
            poly[i][0] = ""
        else:
            poly[i][0] = str(poly[i][1]) + poly[i][0]

    output = [i[0] for i in poly if i[0] != ""]
    send = ""
    for i in range(len(output) - 1):
        if output[i + 1][0] == "-":
            send = send + output[i]
        else:
            send = send + output[i] + "+"
    send = send + output[-1]

    print(send)
    return send
