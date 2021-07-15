def band_name_generator(name):
    return name.capitalize() + name[1:] if name.startswith(name[0]) and name.endswith(name[0]) else 'The ' + name.capitalize() 
