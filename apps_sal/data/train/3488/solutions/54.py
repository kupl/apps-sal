def eval_object(v):
    a = v['a']
    b = v['b']
    c = v['operation']
    return eval('a {} b'.format(c))
