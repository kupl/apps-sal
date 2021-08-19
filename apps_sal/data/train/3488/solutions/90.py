def eval_object(v):
    (op, a, b) = (v['operation'], v['a'], v['b'])
    return {'+': a + b, '-': a - b, '/': a / b, '*': a * b, '%': a % b, '**': a ** b}.get(op, 1)
