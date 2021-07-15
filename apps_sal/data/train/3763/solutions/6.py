def calculator(x, y, op):
    try:
        return eval(f"{x}{op}{y}") if op in "+-*/" else "unknown value"
    except (SyntaxError, NameError, TypeError):
        return "unknown value"

