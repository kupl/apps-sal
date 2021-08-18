import re

find_snake = re.compile("([_])([A-Za-z])")
find_camel = re.compile("([A-Z])")
find_kebab = re.compile("([-])([A-Za-z])")


def is_camel(x): return x != x.lower()
def is_snake(x): return '_' in x
def is_kebab(x): return '-' in x


def to_camel(match):
    return match.group(2).upper()


def to_snake(match):
    return '_' + match.group(1).lower()


def to_kebab(match):
    return '-' + match.group(1).lower()


def change_case(text, target):
    if text == '':
        return ''
    if target not in ['camel', 'kebab', 'snake'] \
            or sum([is_camel(text), is_snake(text), is_kebab(text)]) != 1:
        return None
    if is_camel(text):
        if target == 'snake':
            return re.sub(find_camel, to_snake, text).lower()
        elif target == 'kebab':
            return re.sub(find_camel, to_kebab, text).lower()
    elif is_snake(text):
        if target == 'camel':
            return re.sub(find_snake, to_camel, text)
        elif target == 'kebab':
            return text.replace('_', '-').lower()
    elif is_kebab(text):
        if target == 'snake':
            return text.replace('-', '_').lower()
        elif target == 'camel':
            return re.sub(find_kebab, to_camel, text)
    return text
