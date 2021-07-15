def calculator(a,b,op):
    if op == '/' and b == 0:
        return 'Error! Division by zero!'
    ops = ['+', '-', '*', '/']
    try:
        results = [a + b, a - b, a * b, a / b]
        return results[ops.index(op)]
    except:
        return 'unknown value'
