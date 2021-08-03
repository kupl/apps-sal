import operator


def eval_object(expression):
    mathop = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
        '%': operator.mod,
        '**': operator.pow,
    }
    if not all(isinstance(n, int) for n in (expression['a'], expression['b'])):
        return 0
    else:
        return mathop[expression['operation']](expression['a'], expression['b'])
