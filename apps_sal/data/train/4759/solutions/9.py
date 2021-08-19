def to_acronym(input):
    words = input.split()
    acronym = ''
    for word in words:
        acronym = acronym + word[0].upper()
    return acronym
