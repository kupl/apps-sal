from string import ascii_letters


def make_acronym(phrase):
    acronym = ''
    if isinstance(phrase, str):
        words = phrase.split()
        for word in words:
            for char in word:
                if char in ascii_letters:
                    pass
                else:
                    return 'Not letters'
            acronym += word[0].upper()
        return acronym
    return 'Not a string'
