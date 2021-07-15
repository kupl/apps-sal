def band_name_generator(name):
    return name.title() if len(name) == 1 else name.title()[:-1] + name if name[0] == name[-1] else "The " + name.title()
