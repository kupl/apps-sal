def eval_object(v):
    v = list(map(str, v.values()))
    return eval(v[0] + v[2] + v[1])
