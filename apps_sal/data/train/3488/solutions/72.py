def eval_object(z):
    (a, b, op) = (z[v] for v in ['a', 'b', 'operation'])
    return {'+': a + b, '-': a - b, '/': a / b, '*': a * b, '%': a % b, '**': a ** b}.get(op)
