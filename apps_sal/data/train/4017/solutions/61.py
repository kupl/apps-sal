add, multiply, divide, mod, exponent, subt = ((lambda ope: lambda a, b: eval(str(a) + ope + str(b)))(operator) for operator in ("+", "*", "/", "%", "**", "-"))
