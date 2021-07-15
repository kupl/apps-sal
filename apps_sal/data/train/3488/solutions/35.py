def eval_object(v):
    exp = str(v['a']) + v['operation'] + str(v['b'])
    return eval(exp)
