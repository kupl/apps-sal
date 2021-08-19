def elevator(left, right, call):
    return sorted([('right', right), ('left', left)], key=lambda x: abs(call - x[1]))[0][0]
