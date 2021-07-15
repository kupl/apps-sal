def to_acronym(input):
    words = input.split()
    acronym = ''
    for word in words:
        acronym += word[0]
    return acronym.upper()
