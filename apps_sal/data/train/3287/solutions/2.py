def mouth_size(animal): 
    mouth = {'alligator':'small'}
    return mouth.get(animal.lower(), 'wide')
