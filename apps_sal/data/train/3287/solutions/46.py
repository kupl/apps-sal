def mouth_size(animal):
    new_animal = ''
    for letters in animal:
        if 65 <= ord(letters) <= 90:
            new_animal += chr(ord(letters) + 32)
        else:
            new_animal += letters
    if new_animal == 'alligator':
        return 'small'
    return 'wide'
