
def eval_object(v):
    a = str(v.get('a'))
    b = str(v.get('b'))
    op = v.get('operation')
    return eval(a + op + b)
