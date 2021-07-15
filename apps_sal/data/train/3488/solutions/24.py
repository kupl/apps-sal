import operator
def eval_object(v):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '/': operator.truediv,
        '*': operator.mul,
        '%': operator.mod,
        '**': operator.pow
    }
    return ops.get(v.get('operation'))(v.get('a'), v.get('b'))
