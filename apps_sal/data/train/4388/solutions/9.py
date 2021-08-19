import re


def is_snake_case(identifier):
    return bool(re.fullmatch('[a-z_]+', identifier))


def is_camel_case(identifier):
    return bool(re.fullmatch('([a-z]+[A-Z])+[a-z]*', identifier))


def is_kebab_case(identifier):
    return bool(re.fullmatch('[a-z]*-?', identifier))


def is_mixed_case(identifier):
    if '-' in identifier and '_' in identifier:
        return True
    elif '-' in identifier and [c for c in identifier if c.isupper()]:
        return True
    elif '_' in identifier and [c for c in identifier if c.isupper()]:
        return True


def change_case(identifier, targetCase):
    if not identifier:
        return ''
    elif targetCase not in ['kebab', 'camel', 'snake']:
        return None
    elif is_mixed_case(identifier):
        return None
    elif targetCase == 'snake' and (not is_snake_case(identifier)):
        split = [char for char in re.split('([A-Z]|-)', identifier) if char]
        for (i, char) in enumerate(split):
            if char.isupper():
                split[i] = '_' + char.lower()
            elif char == '-':
                split[i] = '_'
        return ''.join(split)
    elif targetCase == 'camel' and (not is_camel_case(identifier)):
        split = re.split('[_-]', identifier)
        return split[0] + ''.join((word.title() for word in split[1:]))
    elif targetCase == 'kebab' and (not is_kebab_case(identifier)):
        split = re.split('([A-Z]|_)', identifier)
        kebab = split[0]
        for (i, word) in enumerate(split[1:]):
            if not word or word == '_':
                kebab += '-'
            elif word.isupper():
                if kebab[-1] == '-':
                    kebab += word.lower()
                else:
                    kebab += '-' + word.lower()
            else:
                kebab += word.lower()
        return kebab
    else:
        return identifier
