from operator import add, sub, truediv, mul, mod, pow

ops = {'+':add, '-':sub, '/':truediv, '*':mul, '%':mod, '**':pow}

def eval_object(v):
    return ops[v['operation']](v['a'], v['b'])
