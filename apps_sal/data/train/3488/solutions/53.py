def eval_object(v):
    return eval('%d %s %d' % (v['a'], v['operation'], v['b'])) if v['operation'] in '**%/-+' else 1
