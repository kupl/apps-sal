def arithmetic(a, b, operator):
    operators = {'add':'+','subtract':'-','multiply':'*','divide':'/'}
    return eval(str(a)+operators[operator]+str(b))
