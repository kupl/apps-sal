import re


def password(string):
    patterns = ('[A-Z]', '[a-z]', '[0-9]', '.{8,}')
    return all([re.search(pattern, string) for pattern in patterns])
