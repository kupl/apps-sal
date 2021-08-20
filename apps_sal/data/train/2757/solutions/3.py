from re import sub


def check_password(string):
    reduced = sub('[a-z]', 'a', sub('[A-Z]', 'A', sub('[0-9]', '0', sub('[!@#$%^&*?]', '!', string))))
    return 'valid' if 8 <= len(string) <= 20 and set(reduced) == set('aA0!') else 'not valid'
