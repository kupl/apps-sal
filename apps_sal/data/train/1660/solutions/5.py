def simplify(poly):
    
    i = 0
    eq = {}
    length = len(poly)

    while i < length:
        if poly[i] in "+-":
            const = poly[i]
            i += 1
        else:
            const = "+"
        
        while poly[i].isnumeric():
            const += poly[i]
            i += 1
        if not const[-1].isnumeric():
            const += "1"
        
        var = ""
        while i < length and poly[i] not in "-+":
            var += poly[i]
            i += 1
        var = "".join(sorted(var))
        eq[var] = eq.get(var, 0) + int(const)
    
    
    output = ""
    for term in sorted(eq, key = lambda x: (len(x), x)):
        if eq[term] > 1:
            output += "+" + str(eq[term]) + term
        elif eq[term] == 1:
            output += "+" + term
        elif eq[term] == -1:
            output += "-" + term
        elif eq[term] < 0:
            output += str(eq[term]) + term
        
    if output.startswith("+"):
        return output[1:]
    else:
        return output
