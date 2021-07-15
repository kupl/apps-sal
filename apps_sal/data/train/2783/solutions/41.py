def get_grade(*args):
    d={(0,6):'F', (6,7):'D', (7,8):'C', (8,9):'B', (9,11):'A'}
    return next(d[rang] for rang in list(d.keys()) if (sum(args)/len(args))//10 in range(*rang))

