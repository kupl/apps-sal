import re
CHANGES = {'kebab': '-', 'camel': '', 'snake': '_'}
VALID_CASE = re.compile('[A-Z_-]')
CHANGE_CASE = re.compile('[_-][a-z]|[A-Z]')


def change_case(s, targetCase):

    def convertCase(m):
        return (str.upper if targetCase == 'camel' else str.lower)(CHANGES[targetCase] + m.group()[-1])
    if targetCase in CHANGES and len({'A' if c.isalpha() else c for c in VALID_CASE.findall(s)}) <= 1:
        return CHANGE_CASE.sub(convertCase, s)
