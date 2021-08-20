import re
CASES = [('snake', re.compile('\\A[a-z]+(_[a-z]+)+\\Z')), ('kebab', re.compile('\\A[a-z]+(-[a-z]+)+\\Z')), ('camel', re.compile('\\A[a-z]+([A-Z][a-z]*)+\\Z')), ('none', re.compile(''))]


def case_id(c_str):
    for (case, pattern) in CASES:
        if pattern.match(c_str):
            return case
