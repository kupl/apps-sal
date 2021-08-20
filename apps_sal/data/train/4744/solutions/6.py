def band_name_generator(name):
    return 'The ' + name.capitalize() if name[0] != name[-1] else name.capitalize() + name[1:]
