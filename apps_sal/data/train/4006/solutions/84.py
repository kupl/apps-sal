def basic_op(operator, value1, value2):
    k = {'+': value1+value2, '-': value1-value2, '*': value1*value2, '/':value1/value2}
    return k[operator]
