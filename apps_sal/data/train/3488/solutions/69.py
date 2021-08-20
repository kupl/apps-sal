import operator


def eval_object(v):
    return {'+': operator.add, '-': operator.sub, '/': operator.floordiv, '*': operator.mul, '%': operator.mod, '**': operator.pow}[v['operation']](v['a'], v['b'])
