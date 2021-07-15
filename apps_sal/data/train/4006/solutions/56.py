def basic_op(oper, a, b):
    return [a + b, a - b, a * b, a / b][(oper == '-') + 2 * (oper == '*') + 3 * (oper == '/')]
