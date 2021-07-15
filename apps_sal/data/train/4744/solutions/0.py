def band_name_generator(name):
    return name.capitalize()+name[1:] if name[0]==name[-1] else 'The '+ name.capitalize()
