def get_planet_name(id):
    return 'Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune'.split(' ').__getitem__(id-1)
