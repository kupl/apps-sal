def show_me(name):
    return "--" not in name and name[0] != "-" and name[-1] != "-" and name.title() == name and all([c.isalpha() or c == "-" for c in name])
