def make_acronym(phrase):
    try:
        return ''.join(word[0].upper() if word.isalpha() else 0 for word in phrase.split())
    except AttributeError:
        return 'Not a string'
    except TypeError:
        return 'Not letters'
