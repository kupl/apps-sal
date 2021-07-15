from operator import add, sub, truediv, mul, mod, pow
ops = {'+':add, '-':sub, '/':truediv, '*':mul, '%':mod, '**':pow}
one = lambda a,b: 1

def eval_object(v):
    return ops.get(v['operation'], one)(v['a'], v['b'])
