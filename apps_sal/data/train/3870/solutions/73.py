import re


def solve(s):
    ws_indices = [match.span()[0] for match in re.finditer(' ', s)]
    rev_s = list(s[::-1].replace(' ', ''))
    for idx in ws_indices:
        rev_s.insert(idx, ' ')

    return ''.join(rev_s)
