def array_info(x):
    return [[len(x)], [len([a for a in x if type(a) == int]) or None], [len([a for a in x if type(a) == float]) or None], [len([a for a in x if type(a) == str and a != ' ']) or None], [len([a for a in x if a == ' ']) or None]] if len(x) else 'Nothing in the array!'
