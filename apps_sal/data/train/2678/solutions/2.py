op_table = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "*": lambda a,b: a*b,
    "/": lambda a,b: a//b,
    "^": lambda a,b: a**b,
    "%": lambda a,b: a%b,
}

def no_order(equation):
    result = op2 = 0
    func_name = "+"
    
    # dummy add to force prior operation to be run
    formula = equation.replace(" ", "") + "+"
    for ch in formula:
        if ch.isdigit():
            op2 *= 10
            op2 += int(ch)
        elif ch not in op_table:
            return None
        else:
            try:
                result = op_table[func_name](result, op2)
            except ZeroDivisionError:
                return None
            func_name = ch
            op2 = 0

    return result

