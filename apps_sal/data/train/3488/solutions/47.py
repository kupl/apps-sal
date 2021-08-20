def eval_object(v):
    a = v['a']
    b = v['b']
    return {'+': a + b, '-': a - b, '/': a / b, '*': a * b, '%': a % b, '**': a ** b}.get(v['operation'])
