def band_name_generator(name):
    return f"{name}{name[1:]}".capitalize() if name[0] == name[-1] else f"The {name.capitalize()}"
