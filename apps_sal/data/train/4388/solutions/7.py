def discover_case(identifier):
    if identifier is None:
        return None
    elif identifier == '':
        return ''
    elif is_camel(identifier):
        return 'camel'
    elif is_snake(identifier):
        return 'snake'
    elif is_kebab(identifier):
        return 'kebab'
    return None


def is_camel(identifier):
    found_uppercase = False

    for index, ch in enumerate(identifier):
        if not ch.isalnum():
            return False
        elif index != 0 and ch.isalpha() and ch.isupper():
            found_uppercase = True

    return found_uppercase


def is_snake(identifier):
    for ch in identifier:
        if ch.isupper():
            return False

    return '_' in identifier and '-' not in identifier


def is_kebab(identifier):
    for ch in identifier:
        if ch.isupper():
            return False

    return '-' in identifier and '_' not in identifier


def split_words(identifier, case):
    if case == 'camel':
        words = []
        word = ''

        for ch in identifier:
            if ch.isupper():
                words.append(word.lower())
                word = ch
            else:
                word += ch

        words.append(word.lower())
        return words
    elif case == 'snake':
        return identifier.split('_')
    elif case == 'kebab':
        return identifier.split('-')
    else:
        return None


def to_camel(words):
    result = ''
    for index, word in enumerate(words):
        if index == 0:
            result += word
        else:
            result += word.capitalize()
    return result


def to_snake(words):
    return '_'.join(words)


def to_kebab(words):
    return '-'.join(words)


def change_case(identifier, targetCase):
    case = discover_case(identifier)
    if not case:
        return case

    words = split_words(identifier, case)
    if not words:
        return None

    if targetCase == 'camel':
        return to_camel(words)
    elif targetCase == 'snake':
        return to_snake(words)
    elif targetCase == 'kebab':
        return to_kebab(words)
    else:
        return None
