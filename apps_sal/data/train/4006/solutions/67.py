def basic_op(operator, value1, value2):
    if operator == '+':
        def x(a, b): return a + b
        return (x(value1, value2))
    if operator == '-':
        def x(a, b): return a - b
        return (x(value1, value2))
    if operator == '*':
        def x(a, b): return a * b
        return (x(value1, value2))
    if operator == '/':
        def x(a, b): return a / b
        return (x(value1, value2))
