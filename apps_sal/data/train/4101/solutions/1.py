def sum_prod(strexpression):
    strexpression = strexpression.replace("*", " * ").replace("+", " + ")
    equation = [float(x) if x[0].isdigit() else x for x in strexpression.split()]

    for operator in ["*", "+"]:
        while operator in equation:
            pos = equation.index(operator)
            equation[pos - 1] = equation[pos - 1] * equation[pos + 1] if operator == "*" else equation[pos - 1] + equation[pos + 1]
            del equation[pos:pos + 2]

    return '{:.5e}'.format(float(equation[0]))
