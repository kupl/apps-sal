def basic_op(operator, value1, value2):
    return eval("{val1}{operator}{val2}".format(val1=value1, operator=operator, val2=value2))
