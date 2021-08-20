import re


def string_expansion(stg):
    result = ''
    for match in re.finditer('\\d*(^|\\d)([^\\d]+)', stg):
        count = int(match.group(1) or 1)
        for char in match.group(2):
            result = f'{result}{count * char}'
    return result
