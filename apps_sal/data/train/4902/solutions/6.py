def show_me(instname):
    return "Hi, I'm one of those {}s! Have a look at my {}.".format(instname.__class__.__name__, ', '.join(list(instname.__dict__.keys())) if len(list(instname.__dict__.keys())) == 1 else ', '.join(sorted(list(instname.__dict__.keys()))).rpartition(', ')[0] + ' and ' + ', '.join(sorted(list(instname.__dict__.keys()))).rpartition(', ')[2])
