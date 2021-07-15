def nickname_generator(name):
    VOWELS = 'aeiou'
    if len(name) < 4:
        return 'Error: Name too short'
    if name[2] in VOWELS:
        return name[:4]
    else:
        return name[:3]

