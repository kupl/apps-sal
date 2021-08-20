def eval_object(v):
    operations = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '/': lambda a, b: a / b, '*': lambda a, b: a * b, '%': lambda a, b: a % b, '**': lambda a, b: a ** b}
    return operations[v['operation']](v['a'], v['b'])
