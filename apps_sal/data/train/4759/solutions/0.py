def to_acronym(input):
    return ''.join(word[0] for word in input.split()).upper()
