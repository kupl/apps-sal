def is_kebab(s):
    arr = s.split('-')
    res = [part.islower() and '_' not in part and (part != '') for part in arr]
    return all(res)


def is_snake(s):
    arr = s.split('_')
    res = [part.islower() and '-' not in part and (part != '') for part in arr]
    return all(res)


def is_camel(s):
    return '-' not in s and '_' not in s and (not s.islower())


def case_id(c_str):
    if is_kebab(c_str):
        return 'kebab'
    if is_snake(c_str):
        return 'snake'
    if is_camel(c_str):
        return 'camel'
    return 'none'
