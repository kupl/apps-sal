def band_name_generator(name):
    if name[0] == name[-1]:
        return (name + name[1:]).title()
    else:
        return "The " + name.title()
