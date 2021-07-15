def basic_op(o, v1, v2):
    if o == "+":
        return v1+v2
    elif o == "-":
        return v1-v2
    elif o == "*":
        return v1*v2
    elif o == "/":
        return v1/v2
    else:
        return "not recognized"
