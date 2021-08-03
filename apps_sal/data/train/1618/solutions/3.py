def differentiate(equation, point):
    # This can almost certainly be done waaaaay better with regex ...

    # Where are all the signs between terms?
    signs = [i for i in range(len(equation)) if equation[i] in "+-"]
    if not 0 in signs:
        signs = [0] + signs

    # Parse the coefficients and powers (all assumed integers)
    coeffs = []
    powers = []
    for i in range(len(signs)):
        if i + 1 == len(signs):
            term = equation[signs[i]:]
        else:
            term = equation[signs[i]:signs[i + 1]]
        if "^" in term:
            i = term.index("^")
            powers += [int(term.split("^")[1])]
        elif "x" in term:
            powers += [1]
        if "x" in term:
            c = term.split("x")[0]
            if c in ["", "+", "-"]:
                coeffs += [-1 if c == "-" else 1]
            else:
                coeffs += [int(c)]
    return sum([c * p * point**(p - 1) for c, p in zip(coeffs, powers)])
