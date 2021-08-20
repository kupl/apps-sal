from string import ascii_lowercase as ASCII_LOW, ascii_letters as ASCII_LET


def is_kebab_case(str_):
    for char in str_:
        if char not in ASCII_LOW + '-':
            return False
    if '' in str_.split('-'):
        return False
    return True


def is_camel_case(str_):
    for char in str_:
        if char not in ASCII_LET:
            return False
    if str_[0].isupper():
        return False
    return True


def is_snake_case(str_):
    for char in str_:
        if char not in ASCII_LOW + '_':
            return False
    if '' in str_.split('_'):
        return False
    return True


def case_id(c_str):
    for func in (is_kebab_case, is_camel_case, is_snake_case):
        if func(c_str):
            return {'is_kebab_case': 'kebab', 'is_camel_case': 'camel', 'is_snake_case': 'snake'}[func.__name__]
    return 'none'
