def show_me(inst):
    name = inst.__class__.__name__
    atts = ' and'.join(', '.join(sorted(k for k in inst.__dict__)).rsplit(',', 1))
    return "Hi, I'm one of those {}s! Have a look at my {}.".format(name, atts)
