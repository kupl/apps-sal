def to_acronym(input):
    # only call upper() once
    return ''.join(word[0] for word in input.split()).upper()
