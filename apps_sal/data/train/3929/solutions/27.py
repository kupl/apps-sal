def reverse(phrase):
    while '  ' in phrase:
        phrase = phrase.replace('  ', ' ')
    return ' '.join(reversed(phrase.strip().split(' ')))
