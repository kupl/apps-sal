def show_me(instname):
    name = type(instname).__name__ + 's'
    l = list(instname.__dict__.keys())
    l.sort()
    if len(l) == 1:
        string = f'{l[0]}.'
    else:
        s = ', '.join(l[0:-1])
        string = s + f' and {l[-1]}.'
    return f"Hi, I'm one of those {name}! Have a look at my {string}"
