def args_to_string(args):
    s = []
    for i in args:
        if type(i) == str:    s.append(i)
        elif type(i) == list and len(i) == 2:    s.append('-'*(1 if len(i[0]) == 1 else 2)+ ' '.join(i))
        else:    s += i
    return ' '.join(s)
