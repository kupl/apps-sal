def show_me(instname):
    return "Hi, I'm one of those %ss!" % instname.__class__.__name__ + \
        " Have a look at my %s." % ' and '.join(', '.join(sorted(instname.__dict__)).rsplit(', ', 1))
