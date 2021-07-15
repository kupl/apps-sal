def eval_object(v):
    return eval(str(v['a']) + v.get('operation') + str(v['b']))
