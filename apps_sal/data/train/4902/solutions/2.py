def show_me(instname):
    attr = sorted(list(instname.__dict__.keys()))
    attr = ', '.join(attr[:-1]) + ' and '*(len(attr)>=2) + attr[-1]
    return  "Hi, I'm one of those {}s! Have a look at my {}.".format(type(instname).__name__, attr )
