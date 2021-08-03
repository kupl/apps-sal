def mouth_size(animal):
    animal = animal.lower()
    return 'sm' + animal[:3] if animal[3:] == 'igator' else 'wide'
