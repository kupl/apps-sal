def mouth_size(animal):
    animal = animal.casefold()
    return 'small' if 'alligator' in animal else 'wide'
