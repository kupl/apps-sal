def eval_object(v):
    a = v.get('a')
    op = v.get('operation')
    b = v.get('b')
    all = str(a) + op + str(b)
    return eval(all)
