def band_name_generator(name):
    if name[0] == name[-1]:
        return name.title() + name[1:]
    return ("the " + name).title()
