consonants = 'bcdfghjklmnpqrstvwxyz'


def err_bob(stg):
    result = ''
    for (i, char) in enumerate(stg):
        result = f'{result}{char}'
        if char.isalpha() and (not stg[i + 1:i + 2].isalpha()):
            end = 'err' if char in consonants else 'ERR' if char in consonants.upper() else ''
            result = f'{result}{end}'
    return result
