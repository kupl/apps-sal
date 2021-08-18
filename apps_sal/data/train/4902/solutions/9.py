def show_me(instname):
    name, attrs = instname.__class__.__name__, sorted(instname.__dict__)
    if len(attrs) == 1:
        return "Hi, I'm one of those {}s! Have a look at my {}.".format(name, attrs[0])
    return "Hi, I'm one of those {}s! Have a look at my {} and {}.".format(name, ", ".join(attrs[:-1]), attrs[-1])
