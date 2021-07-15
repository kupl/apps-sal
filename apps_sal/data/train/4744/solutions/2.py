def band_name_generator(name):
    if name[0] != name[-1]:
        return "{}{}{}".format("The ", name[0].upper(), name[1:])
    else:
        return "{}{}{}".format(name[0].upper(), name[1:], name[1:])
