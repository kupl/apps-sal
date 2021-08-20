def basic_op(operator, value1, value2):

    def div(a, b):
        return a / b
    operations_mapping = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__, '/': div}
    return operations_mapping[operator](value1, value2)
