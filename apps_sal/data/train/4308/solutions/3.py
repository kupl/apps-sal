def make_acronym(phrase):
    if not isinstance(phrase, str):
        return 'Not a string'
    elif phrase == '':
        return ''
    elif not phrase.replace(' ', '').isalpha():
        return 'Not letters'
    else:
        return ''.join(word[0].upper() for word in phrase.split(' '))
