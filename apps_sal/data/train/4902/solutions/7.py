def show_me(instname):
    return "Hi, I'm one of those {}s! Have a look at my {}.".format(instname.__class__.__name__, ' and '.join(', '.join(sorted(instname.__dict__.keys())).rsplit(', ', 1)))
