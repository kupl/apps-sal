def calculator(x, y, op):
    try:
        if op not in "+-*/" or type(x) not in [int, float] or type(y) not in [int, float]:
            return 'unknown value'
        return eval(f"{x} {op} {y}")
    except TypeError:
        return 'unknown value'
