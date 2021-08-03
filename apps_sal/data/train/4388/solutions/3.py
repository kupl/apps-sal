import re


def change_case(s, case):

    actions = {
        'snake': lambda s: re.sub(r'([A-Z\-])', r'_\1', s).lower().replace('-', ''),
        'camel': lambda s: re.sub(r'(\-|_)(.)', lambda x: x[2].upper(), s),
        'kebab': lambda s: re.sub(r'([A-Z_])', r'-\1', s).lower().replace('_', '')
    }
    return s if not s else sum((any(x.isupper() for x in s), '_' in s, '-' in s)) < 2 \
        and actions.get(case, lambda s: None)(s) or None
