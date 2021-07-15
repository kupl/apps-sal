def monomial(factor, index):
    if factor < 0:
        if factor == -1:
            if not index:
                return " - 1"
            return " - x" if index == 1 else " - x^{}".format(index)
        else:
            if not index:
                return " - {}".format(abs(factor))
            return " - {}x".format(abs(factor)) if index == 1 else " - {}x^{}".format(abs(factor), index)
    else:
        if factor == 1:
            if not index:
                return " + 1"
            return " + x" if index == 1 else " + x^{}".format(index)
        else:
            if not index:
                return " + {}".format(factor)
            return " + {}x".format(factor) if index == 1 else " + {}x^{}".format(factor, index)


def polynomialize(roots):
    zeros, roots2, length = roots.count(0), [r for r in roots if r], len(roots)
    parameters = [1]
    for root in roots2:
        parameters = [1] + [parameters[i+1] - root*parameters[i] for i in range(len(parameters)-1)] + [-parameters[-1]*root]
    return "".join([monomial(param, length-i) for i, param in enumerate(parameters) if param])[3:] + " = 0"
