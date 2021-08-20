def eval_object(v):
    return eval('{0}{1}{2}'.format(v['a'], v['operation'], v['b']))
