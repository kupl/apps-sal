import re


def case_id(c_str):
    if re.match('[a-z]+(-[a-z]+)+$', c_str):
        return 'kebab'
    if re.match('[a-z]+(_[a-z]+)+$', c_str):
        return 'snake'
    if re.match('[a-z]+([A-Z][a-z]+)+$', c_str):
        return 'camel'
    return 'none'
